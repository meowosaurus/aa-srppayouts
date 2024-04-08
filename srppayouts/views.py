"""App Views"""

import re
import requests
import json

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from eveuniverse.models.entities import EveEntity
from eveuniverse.models.universe_2 import EveSolarSystem

from .models import *

def generate_context(request: WSGIRequest): 
    if request.user.has_perm('srppayouts.admin_access'):
        is_admin = True
    else:
        is_admin = False

    context = {"is_admin": is_admin}

    return context


@login_required
@permission_required("srppayouts.basic_access")
def view_payouts(request: WSGIRequest) -> HttpResponse:
    """
    Index view
    :param request:
    :return:
    """

    context = generate_context(request)

    if request.user.has_perm('srppayouts.admin_access'):
        is_admin = True
    else:
        is_admin = False

    # Recalculate data if not available in memory
    if not cache.get('matrix'):
        recalculate_matrix()
    
    matrix = cache.get('matrix')
    
    columns = Reimbursement.objects.all().order_by("index")
    column_width = 100 / (columns.count() + 1)

    context.update({"columns": columns,
                    "column_width": column_width,
                    "matrix": matrix})

    return render(request, "srppayouts/view_payouts.html", context)

@login_required
@permission_required("srppayouts.basic_access")
def my_requests(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    srp_requests = Request.objects.filter(requester_id=request.user.profile.main_character.character_id).order_by('-submitted_on')
    
    context.update({"srp_requests": srp_requests})

    return render(request, "srppayouts/my_requests.html", context)

@login_required
@permission_required("srppayouts.basic_access")
def submit_request(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    if request.method == 'POST':
        killmail = request.POST['killmail']
        ping = request.POST['ping']

        killmail_id, killmail_hash = link_get_esi(killmail)

        esi_get_request_data(request, killmail_id, killmail_hash, ping)

        messages.success(request, "Successfully added reimbursement request!")

    return redirect('srppayouts:my_requests')

@login_required
@permission_required("srppayouts.basic_access")
def delete_request(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    if request.method == 'POST':
        id = request.POST['killmail_id']
        req = Request.objects.get(killmail_id=id)

        if not req.response:
            req.delete()

            messages.success(request, "Successfully deleted request #" + str(id) + "!")
        else:
            messages.error(request, "Unable to delete request: This request has already been processed!")
    else:
        messages.error(request, "Unable to parse data!")

    return redirect('srppayouts:my_requests')

###############################################################

def submit():
    url = 'https://esi.evetech.net/latest/killmails/111406094/a1c152807e0b427635c0f1f39aa1fb746e25cef3/'
    broadcast = "@everyone MAX DREADS ON MEOWSER"

    killmail_id, killmail_hash = link_get_esi(url)

    esi_get_request_data(killmail_id, killmail_hash, broadcast)

def link_get_esi(url: str):
    killmail_id = ""
    killmail_hash = ""

    pattern_zkill = r'https://zkillboard.com/kill/(\d+)/'
    pattern_evetools = r'https://kb.evetools.org/kill/(\d+)'
    pattern_esi = r'https://esi.evetech.net/latest/killmails/(\d+)/([a-f0-9]+)/'

    match_zkill = re.match(pattern_zkill, url)
    match_evetools = re.match(pattern_evetools, url)
    match_esi = re.match(pattern_esi, url)

    if match_zkill:
        killmail_id = match_zkill.groups()[0]

        killmail_hash = zkill_pull_data(killmail_id)
    elif match_evetools:
        killmail_id = match_evetools.groups()[0]

        killmail_hash = zkill_pull_data(killmail_id)
    elif match_esi:
        killmail_id, killmail_hash = match_esi.groups() 

        return killmail_id, killmail_hash
    else:
        print("error")

    return killmail_id, killmail_hash

def esi_get_request_data(req: WSGIRequest, killmail_id: str, killmail_hash: str, ping: str):
    url = "https://esi.evetech.net/latest/killmails/" + killmail_id + "/" + killmail_hash + "/"

    headers = {
        'Content-Encoding': 'gzip',
    }

    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        data = request.json()

        new_request = Request()

        killmail_time = data['killmail_time']
        solar_system_id = data['solar_system_id']
        solar_system_name = EveEntity.objects.resolve_name(solar_system_id)
        character_id = data['victim']['character_id']
        character_name = esi_get_character_name(str(character_id))
        corporation_id = data['victim']['corporation_id']
        corporation_name = esi_get_corporation_name(str(corporation_id))
        alliance_id = data['victim']['alliance_id']
        alliance_name = esi_get_alliance_name(str(alliance_id))
        ship_type_id = data['victim']['ship_type_id']
        ship_type_name = EveEntity.objects.resolve_name(ship_type_id)

        new_request.killmail_id = killmail_id
        new_request.killmail_hash = killmail_hash
        new_request.killmail_time = killmail_time
        new_request.killmail_solar_id = solar_system_id
        new_request.killmail_solar_name = solar_system_name
        new_request.character_id = character_id
        new_request.character_name = character_name
        new_request.corporation_id = corporation_id
        new_request.corporation_name = corporation_name
        new_request.alliance_id = alliance_id
        new_request.alliance_name = alliance_name
        new_request.ship_id = ship_type_id
        new_request.ship_name = ship_type_name
        new_request.esi_link = url
        new_request.requester_id = req.user.profile.main_character.character_id
        new_request.requester_name = req.user.profile.main_character.character_name
        new_request.ping = ping

        new_request.save()
    else:
        print("error")

def esi_get_character_name(character_id: str) -> str:
    url = "https://esi.evetech.net/latest/characters/" + character_id + "/?datasource=tranquility"

    headers = {
        'Content-Encoding': 'gzip',
    }

    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        data = request.json()

        return data['name']
    else:
        print("Error esi get character name")

        return ""

def esi_get_corporation_name(corporation_id: str) -> str:
    url = "https://esi.evetech.net/latest/corporations/" + corporation_id + "/?datasource=tranquility"

    headers = {
        'Content-Encoding': 'gzip',
    }

    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        data = request.json()

        return data['name']
    else:
        print("Error esi get corporation name")

        return ""

def esi_get_alliance_name(alliance_id: str) -> str:
    url = "https://esi.evetech.net/latest/alliances/" + alliance_id + "/?datasource=tranquility"

    headers = {
        'Content-Encoding': 'gzip',
    }

    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        data = request.json()

        return data['name']
    else:
        print("Error esi get corporation name")

        return ""

def zkill_pull_data(killmail_id: str):
    killmail_hash = ""

    zkill_api = "https://zkillboard.com/api/killID/" + killmail_id + "/"

    # According to zKillboard API rules
    headers = {
        'Content-Encoding': 'gzip',
        #TODO
        'User-Agent': 'Alliance Auth: aa-srppayouts plugin Email: info@bjsonnen.de (Under development)',
    }

    res = requests.get(zkill_api, headers=headers)
    if res.status_code == 200:
        data = res.json()

        killmail_data = data[0]
        killmail_hash = killmail_data['zkb']['hash']
    else:
        print("Error, unable to pull data from zKillboard.com API: " + response)

    return killmail_hash

def check_url_zkill(url: str) -> bool:
    pattern = r'https://zkillboard.com/kill/(\d+)/'

    match = re.match(pattern, url)

    if match:
        return True
    else:
        return False

def check_url_esi(url: str) -> bool:
    pattern = r'https://esi.evetech.net/latest/killmails/(\d+)/([a-f0-9]+)/'

    match = re.match(pattern, url)

    if match:
        return True
    else:
        return False

def check_url_evetools(url: str) -> bool:
    pattern = r'https://kb.evetools.org/kill/(\d+)'

    match = re.match(pattern, url)

    if match: 
        return True
    else: 
        return False

### ADMIN

@login_required
@permission_required("srppayouts.admin_access")
def force_recalc(request: WSGIRequest) -> HttpResponse:

    print("User " + request.user.profile.main_character.character_name + " forced a recalculation of the srp payouts table!")

    recalculate_matrix()

    return redirect('srppayouts:view_payouts')

"""App Views"""

import re
import requests
from datetime import datetime

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *

def generate_context(request: WSGIRequest):

    open_requests_count = 0

    if request.user.has_perm('srppayouts.use_access'):
        is_user = True
    else:
        is_user = False

    if request.user.has_perm('srppayouts.fcing_access'):
        is_fc = True
    else:
        is_fc = False

    if request.user.has_perm('srppayouts.reimbursement_access'):
        open_requests_count = Request.objects.filter(review=None).count()
        is_reimburser = True
    else:
        is_reimburser = False

    if request.user.has_perm('srppayouts.admin_access'):
        is_admin = True
    else:
        is_admin = False

    context = {"is_user": is_user,
               "is_fc": is_fc,
               "is_reimburser": is_reimburser,
               "is_admin": is_admin,
               "open_requests_count": open_requests_count}

    return context


@login_required
@permission_required("srppayouts.basic_access")
def view_payouts(request: WSGIRequest) -> HttpResponse:
    """
    Index view
    :param request:
    :return:
    """

    if request.user.has_perm('srppayouts.admin_access'):
        is_admin = True
    else:
        is_admin = False

    context = generate_context(request)

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
@permission_required("srppayouts.use_access")
def my_requests(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    user_requests = Request.objects.filter(requester=request.user).order_by('-killmail_time')

    user_requests_count = user_requests.count()

    matrix = []
    row = []
    for index, i in enumerate(user_requests):
        row.append(i)

        if (index + 1) % 4 == 0:
            matrix.append(row)
            row = []

    if row:
        remaining_elements = int(4 - len(row))
        
        for i in range(remaining_elements):
            row.append(None)

        matrix.append(row)

    print(matrix)

    context.update({'user_requests': user_requests,
                    'user_requests_count': user_requests_count,
                    'test_matrix': matrix})

    return render(request, "srppayouts/requests.html", context)

@login_required
@permission_required("srppayouts.use_access")
def submit_request(request: WSGIRequest) -> HttpResponse:

    killmail = request.POST.get("killmail", "")
    broadcast = request.POST.get("broadcast", "")

    ZKILLBOARD_REGEX = r'^https://zkillboard\.com/kill/(?P<kill_id>\d+)/$'
    EVETOOLS_REGEX = r'^https://kb\.evetools\.org/kill/(?P<kill_id>\d+)/$'
    ESI_REGEX = r'^https://esi\.evetech\.net/latest/killmails/(?P<kill_id>\d+)/(?P<kill_hash>[a-fA-F0-9]+)/$'

    killmail_id = 0
    killmail_hash = ""

    headers = {
        'Accept-Encoding': 'gzip',
        'User-Agent': 'Development environment, Alliance Auth, plugin: aa-srppayouts, branch v1.1, maintainer: info@bjsonnen.de'
    }

    # Get the killmail id and hash
    if re.match(ZKILLBOARD_REGEX, killmail):
        kill_match = re.match(ZKILLBOARD_REGEX, killmail)

        killmail_id = kill_match.group('kill_id')

        url = "https://zkillboard.com/api/killID/" + killmail_id + "/"

        response = requests.get(url, headers=headers)

        data = response.json()

        killmail_hash = data[0]['zkb']['hash']
    elif re.match(EVETOOLS_REGEX, killmail):
        kill_match = re.match(EVETOOLS_REGEX, killmail)

        killmail_id = kill_match.group('kill_id')

        url = "https://zkillboard.com/api/killID/" + killmail_id + "/"

        response = requests.get(url, headers=headers)

        data = response.json()

        killmail_hash = data[0]['zkb']['hash']
    elif re.match(ESI_REGEX, killmail):
        kill_match = re.match(ESI_REGEX, killmail)

        killmail_id = kill_match.group('kill_id')
        killmail_hash = kill_match.group('kill_hash')

        print("bla")
    else:
        # TODO: Send an erorr to the users new view
        print("Error")

    esi_url = "https://esi.evetech.net/latest/killmails/" + killmail_id + "/" + killmail_hash + "/"

    esi_headers = {
        'Accept-Encoding': 'gzip'
    }

    print(killmail_id)
    print(killmail_hash)

    esi_response = requests.get(esi_url, headers=esi_headers)
    esi_data = esi_response.json()

    # To get the character name and corporation ID from the character ID
    esi_player_public_info = requests.get("https://esi.evetech.net/latest/characters/" + str(esi_data['victim']['character_id']) + "/?datasource=tranquility", 
                                           headers=esi_headers)
    player_public_info_data = esi_player_public_info.json()

    # To get the corporation name and alliance ID from the corporation ID
    esi_corp_public_info = requests.get("https://esi.evetech.net/latest/corporations/" + str(esi_data['victim']['corporation_id']) + "/?datasource=tranquility",
                                        headers=esi_headers)
    corp_public_info_data = esi_corp_public_info.json()

    # To get the alliance name from the alliance ID
    esi_alliance_public_info = requests.get("https://esi.evetech.net/latest/alliances/" + str(esi_data['victim']['alliance_id']) + "/?datasource=tranquility",
                                            headers=esi_headers)
    corp_alliance_info_data = esi_alliance_public_info.json()

    # To get the ship name from the ship ID
    esi_ship_info = requests.get("https://esi.evetech.net/latest/universe/types/" + str(esi_data['victim']['ship_type_id']) + "/?datasource=tranquility&language=en",
                                 headers=esi_headers)
    esi_ship_data = esi_ship_info.json()

    # To get the solar system name and constellation ID from the solar system ID
    esi_solar_info = requests.get("https://esi.evetech.net/latest/universe/systems/" + str(esi_data['solar_system_id']) + "/?datasource=tranquility&language=en",
                                   headers=esi_headers)
    esi_solar_data = esi_solar_info.json()

    # To get the constellation name and region ID from the constellation ID
    esi_const_info = requests.get("https://esi.evetech.net/latest/universe/constellations/" + str(esi_solar_data['constellation_id']) + "/?datasource=tranquility&language=en",
                                   headers=esi_headers)
    esi_const_data = esi_const_info.json()

    # To get the region name from the region ID
    esi_region_info = requests.get("https://esi.evetech.net/latest/universe/regions/" + str(esi_const_data['region_id']) + "/?datasource=tranquility&language=en",
                                    headers=esi_headers)
    esi_region_data = esi_region_info.json()

    new_srp_request = Request()
    new_srp_request.requester = request.user
    new_srp_request.killmail_id = killmail_id
    new_srp_request.killmail_hash = killmail_hash
    new_srp_request.killmail_time = esi_data['killmail_time']
    new_srp_request.killmail_amount = data[0]['zkb']['totalValue']
    new_srp_request.ship_id = esi_data['victim']['ship_type_id']
    new_srp_request.ship_name = esi_ship_data['name']
    new_srp_request.character_id = esi_data['victim']['character_id']
    new_srp_request.character_name = player_public_info_data['name']
    new_srp_request.corporation_id = esi_data['victim']['corporation_id']
    new_srp_request.corporation_name = corp_public_info_data['name']
    new_srp_request.alliance_id = esi_data['victim']['alliance_id']
    new_srp_request.alliance_name = corp_alliance_info_data['name']
    new_srp_request.system_id = esi_data['solar_system_id']
    new_srp_request.system_name = esi_solar_data['name']
    new_srp_request.constellation_id = esi_solar_data['constellation_id']
    new_srp_request.constellation_name = esi_const_data['name']
    new_srp_request.region_id = esi_const_data['region_id']
    new_srp_request.region_name = esi_region_data['name']
    new_srp_request.broadcast = broadcast
    new_srp_request.data = esi_data
    new_srp_request.save()

    return redirect('srppayouts:requests')

### FC ###

@login_required
def all_links(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    all_reqs = Request.objects.all.order_by('requested_on')

    context.update({'all_requests': all_reqs})

    return render(request, "srppayouts/fc/all_links.html", context)

### REIMBURSER ###

@login_required
def open_requests(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    open_reqs = Request.objects.filter(review=None).order_by('requested_on')

    context.update({'open_requests': open_reqs})

    return render(request, "srppayouts/reimburser/open_requests.html", context)
    
@login_required
def all_requests(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    return render(request, "srppayouts/reimburser/all_requests.html", context)

@login_required
def statistics(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    return render(request, "srppayouts/reimburser/statistics.html", context)

### ADMIN ###

@login_required
@permission_required("srppayouts.admin_access")
def force_recalc(request: WSGIRequest) -> HttpResponse:

    print("User " + request.user.profile.main_character.character_name + " forced a recalculation of the srp payouts table!")

    recalculate_matrix()

    return redirect('srppayouts:view_payouts')

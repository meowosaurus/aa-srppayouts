"""App Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *

def generate_context(request: WSGIRequest):

    if request.user.has_perm('srppayouts.use_access'):
        is_user = True
    else:
        is_user = False

    if request.user.has_perm('srppayouts.fcing_access'):
        is_fc = True
    else:
        is_fc = False

    if request.user.has_perm('srppayouts.reimbursement_access'):
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
               "is_admin": is_admin}

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

    return render(request, "srppayouts/requests.html", context)

### FC ###

@login_required
def all_links(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    return render(request, "srppayouts/fc/all_links.html", context)

### REIMBURSER ###

@login_required
def open_requests(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

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

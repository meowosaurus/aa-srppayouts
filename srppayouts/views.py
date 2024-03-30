"""App Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

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

def my_requests(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    return render(request, "srppayouts/my_requests.html", context)

def submit_request(request: WSGIRequest) -> HttpResponse:

    context = generate_context(request)

    return render(request, "srppayouts/submit_request.html", context)

### ADMIN

@login_required
@permission_required("srppayouts.admin_access")
def force_recalc(request: WSGIRequest) -> HttpResponse:

    print("User " + request.user.profile.main_character.character_name + " forced a recalculation of the srp payouts table!")

    recalculate_matrix()

    return redirect('srppayouts:view_payouts')

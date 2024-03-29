"""App Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *

@login_required
@permission_required("srppayouts.basic_access")
def index(request: WSGIRequest) -> HttpResponse:
    """
    Index view
    :param request:
    :return:
    """

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

    context = {"columns": columns,
               "column_width": column_width,
               "matrix": matrix,
               "is_admin": is_admin}

    return render(request, "srppayouts/index.html", context)

@login_required
@permission_required("srppayouts.admin_access")
def force_recalc(request: WSGIRequest) -> HttpResponse:

    print("User " + request.user.profile.main_character.character_name + " forced a recalculation of the srp payouts table!")

    recalculate_matrix()

    return redirect('srppayouts:index')

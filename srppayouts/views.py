"""App Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

@login_required
@permission_required("srppayouts.basic_access")
def index(request: WSGIRequest) -> HttpResponse:
    """
    Index view
    :param request:
    :return:
    """

    # Recalculate data if not available in memory
    if not cache.get('matrix'):
        recalculate_matrix()
    
    matrix = cache.get('matrix')
    
    columns = Reimbursement.objects.all().order_by("index")
    column_width = 100 / (columns.count() + 1)

    context = {"columns": columns,
               "column_width": column_width,
               "matrix": matrix}

    return render(request, "srppayouts/index.html", context)

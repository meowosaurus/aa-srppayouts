"""App URLs"""

# Django
from django.urls import path

# AA srppayouts App
from srppayouts import views

app_name: str = "srppayouts"

urlpatterns = [
    path("view-payouts/", views.view_payouts, name="view_payouts"),
    path("my-requests/", views.my_requests, name="my_requests"),

    path("submit-request/", views.submit_request, name="submit_request"),
    path("delete-request/", views.delete_request, name="delete_request"),
    path("force-recalc/", views.force_recalc, name="force_recalc"),
]

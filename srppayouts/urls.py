"""App URLs"""

# Django
from django.urls import path

# AA srppayouts App
from srppayouts import views

app_name: str = "srppayouts"

urlpatterns = [
    # User
    path("", views.view_payouts, name="view_payouts"),
    path("my-requests/", views.my_requests, name="my_requests"),
    path("view-statistics/", views.view_statistics, name="view_statistics"),

    # User POST
    path("submit-request/", views.submit_request, name="submit_request"),
    path("delete-request/", views.delete_request, name="delete_request"),

    # Reimburse
    path("reimburse/open-requests/", views.reimburse_open_requests, name="reimburse_open_requests"),
    path("reimburse/closed-requests/", views.reimburse_closed_requests, name="reimburse_closed_requests"),

    # Manager
    path("editor/change-payouts/", views.manager_change_payouts, name="manager_change_payouts"),

    # Admin POST
    path("admin/force-recalc/", views.force_recalc, name="admin_force_recalc"),
]

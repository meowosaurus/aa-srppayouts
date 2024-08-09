"""App URLs"""

# Django
from django.urls import path

# AA srppayouts App
from srppayouts import views

app_name: str = "srppayouts"

urlpatterns = [
    path("", views.view_payouts, name="view_payouts"),
    path("requests/", views.my_requests, name="requests"),

    path("fc/all/", views.all_links, name="fc_all_links"),

    path("reimburser/open/", views.open_requests, name="reimburser_open_requests"),
    path("reimburser/all/", views.all_requests, name="reimburser_all_requests"),
    path("reimburser/statistics/", views.statistics, name="reimburser_statistics"),

    path("force_recalc/", views.force_recalc, name="force_recalc"),
]

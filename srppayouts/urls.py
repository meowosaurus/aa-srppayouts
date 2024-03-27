"""App URLs"""

# Django
from django.urls import path

# AA srppayouts App
from srppayouts import views

app_name: str = "srppayouts"

urlpatterns = [
    path("", views.index, name="index"),
]

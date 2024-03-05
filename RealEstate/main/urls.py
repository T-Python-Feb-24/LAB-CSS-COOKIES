from . import views
from django.urls import path

app_name = 'mainApp'

urlpatterns = [
    path("", views.home_page, name="home_page")
]
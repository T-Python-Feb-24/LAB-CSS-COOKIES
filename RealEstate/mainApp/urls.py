from . import views
from django.urls import path

app_name = 'mainApp'

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("mode/dark/", views.dark_mode, name="dark_mode"),
    path("mode/light/", views.light_mode, name="light_mode"),
    path("properties/", views.properties_page, name="properties_page"),
    path("contact/", views.contact_us_page, name="contact_us_page"),
]

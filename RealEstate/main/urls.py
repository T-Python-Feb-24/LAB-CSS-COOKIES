from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("mode/large/", views.mode_dark_view, name="mode_dark_view"),
    path("mode/small/", views.mode_light_view, name="mode_light_view"),
    path("properties/", views.properites_view, name="properites_view"),
    path("contact/", views.contact_view,name="contact_view"),
]
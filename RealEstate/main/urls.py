from django.urls import path
from . import views


app_name = "main"


urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("prop/", views.prop_view, name="prop_view"),
    path("cont/", views.cont_view, name="cont_view"),
    path("", views.home_view, name="home_view"),
]

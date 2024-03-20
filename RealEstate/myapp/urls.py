from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('properties/', views.properties_view, name='properties'),
    path("", views.properties_view, name="properties"),
    path("mode/dark/", views.dark_mode_view, name="dark_mode_view"),
    path("mode/light/", views.light_mode_view, name="light_mode_view"), 
]

from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('properties/', views.properties_view, name='properties'),
    path("", views.properties_view, name="properties"),
    path('mode-dark/', views.mode_dark, name='mode_dark'), 
    path('mode_light/', views.mode_light, name='mode_light'),  
]

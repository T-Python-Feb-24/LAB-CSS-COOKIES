from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('properties/', views.home, name='properties'),
    path("mode/dark/", views.mode_dark, name="mode_large_view"),
    path("mode/light/", views.mode_light, name="mode_small_view"),
]

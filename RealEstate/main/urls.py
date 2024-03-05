from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('mode/light/', views.light_mode, name='light_mode'),
    path('mode/dark/', views.dark_mode, name='dark_mode'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'),
    
]
from . import views
from django.urls import path

app_name = 'real_estate'

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('properties/', views.properties_page, name = 'properties_page'),
    path('contact/', views.contact_page, name = 'contact_page'),
    path('mode/light/', views.light_mode, name='light_mode'),
    path('mode/dark/', views.dark_mode, name='dark_mode'),

]

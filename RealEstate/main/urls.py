from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('property/', views.property_page, name='property_page'),
    path('contact/', views.contact_page, name='contact_page'),  
    path("mode/dark/", views.dark_mode, name="dark_mode"),
    path("mode/light/", views.light_mode, name="light_mode"),  
]
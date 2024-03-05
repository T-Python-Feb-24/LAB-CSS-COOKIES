from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('properties/', views.properties, name='properties'),
]

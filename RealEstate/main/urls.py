from . import views
from django.urls import path 

app_name="main"

urlpatterns = [
   path("" , views.home , name="home_page"),
   path("contact/" , views.contact , name="contact_page"),
   path("properties/", views.properties , name="properties"),
   path("dark/home", views.darkhome,name="dark_page"),
   path("mode/dark/" , views.dark_mode,name="darkview"),
   path("mode/light/" , views.light_mode,name="lightview"),
]
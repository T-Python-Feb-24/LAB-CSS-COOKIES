from . import views
from django.urls import path

app_name="main"

urlpatterns=[
    path("",views.home_page,name="home_page"),
     path("/properties",views.properties_Basis,name="properties_Basis"),
      path("/contact",views.contact_Basis,name="contact_Basis"),
       
]
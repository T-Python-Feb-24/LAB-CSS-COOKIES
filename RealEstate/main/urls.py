from . import views
from django.urls import path

App_name='main'

urlpatterns =[
    path('',views.home_page,name="home_page")
]
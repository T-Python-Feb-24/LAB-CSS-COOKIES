from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
        path("", views.index_page, name="index_page"),
        path("properties/",views.properties_page, name="properties_page"),
        path("contact/",views.contact_page, name="contact_page"),
        path('mode/light/', views.light_mode, name='light_mode'),
        path('mode/dark/', views.dark_mode, name='dark_mode'),
]      
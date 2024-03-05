from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
        path("", views.index_page, name="index_page"),
        path("properties/",views.properties_page, name="properties_page"),
        path("contact/",views.contact_page, name="contact_page")
]      
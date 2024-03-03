from django.template import loader
from django.http import HttpResponse, HttpRequest


def home_page(request: HttpRequest):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def properties_page(request: HttpRequest):
    template = loader.get_template('properties.html')
    return HttpResponse(template.render())


def about_page(request: HttpRequest):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def contactus_page(request: HttpRequest):
    template = loader.get_template('contactus.html')
    return HttpResponse(template.render())

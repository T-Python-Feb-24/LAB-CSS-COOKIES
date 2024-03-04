from django.template import loader
from django.shortcuts import redirect,render
from django.http import HttpRequest


def home_page(request: HttpRequest):
    # template = loader.get_template('index.html')

    return render(request,"index.html")


def mode_light(request: HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "False")

    return response


def mode_dark(request: HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("mode", "True")

    return response


def properties_page(request: HttpRequest):
   
    return render(request, "properties.html")


def about_page(request: HttpRequest):
   
    return render(request,"about.html")


def contactus_page(request: HttpRequest):
    return render(request, "contactus.html")

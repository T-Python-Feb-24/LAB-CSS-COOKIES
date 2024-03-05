from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#Create your views here.
def home_page(request:HttpRequest): 
    return render(request, 'main/home.html')

def page(request:HttpRequest):
    print(request.COOKIES)
    return render(request, "main/base.html")


def properties(request:HttpRequest): 
    return render(request, 'main/properties.html')


def terms_view(request:HttpRequest):

    return render(request, "main/terms.html")


def mode_large_view(request:HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("DarkMode", "True", max_age=60*60*24*7)
    return response


def mode_small_view(request:HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("DarkMode", "False")

    return response
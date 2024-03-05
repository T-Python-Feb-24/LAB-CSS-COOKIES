from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.


def main_view(request:HttpRequest):
    print(request.COOKIES)
    return render(request, "main/home_page.html")

def mode_dark_view(request:HttpRequest):

    response = redirect("main:main_view")
    response.set_cookie("modeDark", "True", max_age=60*60*24*7)

    return response


def mode_light_view(request:HttpRequest):

    response = redirect("main:main_view")
    response.set_cookie("modeDark", "False")

    return response

def properites_view(reguest:HttpRequest):
     
    
     properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
     context = {
        "properties" : properties
    }

     return render(reguest , "main/properties_page.html",context)

def contact_view(request: HttpRequest):
    return render(request, "main/contact_page.html")  
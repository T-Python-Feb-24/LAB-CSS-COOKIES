from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse
# Create your views here.
def home_page(request:HttpRequest):
    return render(request,'main/index.html')

def home_view(request: HttpRequest):


    return render(request, "main/index.html")


def contact_view(request: HttpRequest):

    return render(request, "main/contact.html")


def dark_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "light")

    return response


def bootstrap_view(request: HttpRequest):

    return render(request, "main/boostrap.html")

def properties_view(request: HttpRequest):

    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]

    return render(request, "main/properties.html", {"properties" : properties})

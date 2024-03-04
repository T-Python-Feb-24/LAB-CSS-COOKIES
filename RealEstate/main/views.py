from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
def home_page(request:HttpRequest):
    return render(request, 'main/home.html')

def property_page(request:HttpRequest):

    context = {'properties':properties}
    return render(request, 'main/property.html', context)

def contact_page(request:HttpRequest):
    return render(request, 'main/contact.html')

def dark_mode(request:HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("DarkMode", "True", max_age=60*60*24*7)

    return response

def light_mode(request:HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("DarkMode", "False")

    return response
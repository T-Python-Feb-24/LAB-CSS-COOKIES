from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_page(request:HttpRequest): 
    return render(request, 'mainApp/home.html')

def dark_mode(request:HttpRequest):
    response = redirect('mainApp:home_page')
    response.set_cookie("dark_mode", "True", max_age=60*60)
    return response

def light_mode(request:HttpRequest):
    response = redirect('mainApp:home_page')
    response.set_cookie("dark_mode", "False")
    return response

def properties_page(request:HttpRequest):
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    return render(request, "mainApp/properties.html", {'properties': properties})

def contact_us_page(request:HttpRequest):
    return render(request, "mainApp/contact.html")


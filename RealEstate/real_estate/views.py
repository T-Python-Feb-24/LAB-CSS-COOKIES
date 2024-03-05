from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse

def home_page(request:HttpRequest):
    
    return render(request, 'real_estate/home_page.html')

def properties_page(request:HttpRequest):

    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]

    context = {
        "properties" : properties,
    }

    return render(request, 'real_estate/properties_page.html', context)


def contact_page(request:HttpRequest):
    
    return render(request, 'real_estate/contact_page.html')


def light_mode(request:HttpRequest):
    response = redirect('real_estate:home_page')
    response.set_cookie('darkMode', 'False')
    return response

def dark_mode(request:HttpRequest):
    response = redirect('real_estate:home_page')
    response.set_cookie('darkMode', 'True')
    return response
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_page(request:HttpRequest):

    return render(request,"main/index.html")



def contact_page(request:HttpRequest):

    return render(request,"main/contact.html")



def properties_page(request:HttpRequest):

    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]

    context ={
        "properties" : properties,
    }
    return render(request,"main/properties.html", context)
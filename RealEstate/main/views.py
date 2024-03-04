from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]

def home_page(request:HttpRequest):
    return render(request, "main/home.html")


def contact_Basis(request:HttpRequest):
    return render (request, "main/contact_page.html")


def properties_Basis(request:HttpRequest):
    context={'properties':properties}
    return render(request,'main/properties.html',context)

# Create your views here.

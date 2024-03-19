from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
# Create your views here.

properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
def home_page(request:HttpRequest):
    return render(request,'main/home_page.html')

def properties_page(request:HttpRequest):
    context = {'properties':properties}
    return render(request,'main\properties.html',context)

def contact_page(request:HttpRequest):
    return render(request,'main/contact.html')


def dark_mode(requset: HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "dark")

    return response


def light_mode(requset: HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "light")

    return response
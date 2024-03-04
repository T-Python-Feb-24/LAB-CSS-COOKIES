from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home(request: HttpRequest):
 return render(request,"main/home.html")

def darkhome(request: HttpRequest):
 return render(request,"main/dark.html")

def contact(request: HttpRequest):
 return render(request,"main/contact.html")

def properties(request: HttpRequest):
 return render(request,"main/properties.html" , contaxt)

contaxt={
 properties:[
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
}


def dark_mode(request: HttpRequest):
  response = redirect("main:dark_page")
  response.set_cookie("modedark", "True", max_age=60*60*24*7)
  return response

def light_mode(request: HttpRequest):
  response = redirect("main:home_page")
  response.set_cookie("modedark", "False", max_age=60*60*24*7)
  return response
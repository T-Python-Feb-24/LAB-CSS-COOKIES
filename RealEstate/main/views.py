from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home_page(request:HttpRequest):
    return render(request,'main/home_page.html')

def properties_page(request:HttpRequest):
    return render(request,'main\properties.html')

def contact_page(request:HttpRequest):
    return render(request,'main/contact.html')
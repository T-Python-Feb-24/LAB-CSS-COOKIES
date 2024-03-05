

from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import date
# Create your views here.
def index_page(request:HttpRequest):

    return render(request,"main/index.html")


def properties_page(request:HttpRequest):
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    return render(request, 'main/home.html', {'properties': properties})

def contact_page(request:HttpRequest):
    return render(request,"main/contact_page.html")





from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_view(request:HttpRequest):


    return render(request, "main/home.html")

#def properties(request:HttpRequest):

#    return render(request, "main/properties.html")

def properties_view(request):
    # List of properties with title and image
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    # Render the "Properties.html" template with properties data
    return render(request, "myapp/Properties.html", {'properties': properties})



def dark_mode_view(requset: HttpRequest):

    response = redirect("myapp:home")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("myapp:home")
    response.set_cookie("mode", "light")

    return response

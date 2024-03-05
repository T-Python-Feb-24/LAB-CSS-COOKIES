# from django.shortcuts import render,redirect
# from django.http import HttpRequest, HttpResponse
# def home(request):
    
#     return render(request, 'main/home.html', {'properties': properties})



# def properties(request):
#    properties = [
#         {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
#         {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
#         {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
#         {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
#     ]
#    return render(request, 'main/properties.html', {'properties': properties})
# context = {
#         "properties" : properties,
#     }

# def contact(request):
#     return render(request, 'main/contact.html')

# def light_mode(request:HttpRequest):
#     response = redirect('main:home_page')
#     response.set_cookie('darkMode', 'False')
#     return response

# def dark_mode(request:HttpRequest):
#     response = redirect('main:home_page')
#     response.set_cookie('darkMode', 'True')
#     return response
from django.shortcuts import render, redirect

# الدالة المحدثة لـ home
def home(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/home.html', {'properties': properties})

# الدالة المحدثة لـ properties
def properties(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/properties.html', {'properties': properties})

def contact(request):
    return render(request, 'main/contact.html')

# الدالتين المحدثتين لـ light_mode و dark_mode
def light_mode(request):
    response = redirect('main:home') # تحديث هنا
    response.set_cookie('darkMode', 'False')
    return response

def dark_mode(request):
    response = redirect('main:home') # تحديث هنا
    response.set_cookie('darkMode', 'True')
    return response

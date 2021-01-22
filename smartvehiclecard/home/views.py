from customer.models import Customer
from customer.forms import CustomerForm
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, "homepage/home.html")

def login(request):
    return render(request, "homepage/login.html")

def signup(request):
    return render(request, 'homepage/signup.html')

# def profile(request):
# return render(request, 'homepage profile.html')

# def settings(request):
#     return render(request, 'homepage/settings.html')
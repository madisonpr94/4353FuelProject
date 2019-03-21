from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def index_page(request):
    return render(request, 'FuelProjectDev/index.html')

def login_page(request):
    return render(request, 'FuelProjectDev/login.html')

def profile_page(request):
    return render(request, 'FuelProjectDev/profile.html')

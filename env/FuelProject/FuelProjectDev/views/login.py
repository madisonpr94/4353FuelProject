from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def login_page(request):
    context = {}

    return render(request, 'FuelProjectDev/login.html', context)

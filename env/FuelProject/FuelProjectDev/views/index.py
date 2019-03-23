from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def index_page(request):
    return render(request, 'FuelProjectDev/index.html')

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def history_page(request):
    return render(request, 'FuelProjectDev/history.html')

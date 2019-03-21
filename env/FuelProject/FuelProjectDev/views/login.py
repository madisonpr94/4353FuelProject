from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def login_page(request, redirect_not_logged_in=False):
    context = {}
    if redirect_not_logged_in:
        context["announce_must_log_in"] = True

    return render(request, 'FuelProjectDev/login.html', context)

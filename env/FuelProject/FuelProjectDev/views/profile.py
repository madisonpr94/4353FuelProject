from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required


@login_required
def profile_page(request):
    return render(request, 'FuelProjectDev/profile.html')

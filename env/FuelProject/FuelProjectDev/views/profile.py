from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django import forms

@login_required
def profile_page(request):
    context ={}
    states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
    ]
    context["states"] = states

    if request.method == 'POST':
        
        context["full_name"] = request.POST['full_name'],
        context["address_1"] = request.POST['address_1'],
        context["address_2"] = request.POST['address_2'],
        context["city_name"] = request.POST['city_name'],
        
        context["state"] = request.POST['state'],
        context["zip_code"] = request.POST['zip_code'],
    

    return render(request, 'FuelProjectDev/profile.html', context, content_type='text/html')

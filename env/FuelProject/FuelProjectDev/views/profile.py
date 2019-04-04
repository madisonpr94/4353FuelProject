from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django import forms

from ..models.profile_info import ProfileInfo

msg_update_profile = "You must complete your profile before ordering."
msg_profile_updated = "Profile updated successfully."


def html_escape(text):
    table = {
            "&": "&amp;",
            ">": "&gt;",
            "<": "&lt;",
            '"': "&quot;",
            "'": "&apos;",
    }
    return "".join(table.get(c, c) for c in text)


@login_required
def profile_page(request):
    context = {}
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
    context["state"] = "none"

    if request.method == 'POST':
        # Sanitize input
        full_name = html_escape(request.POST['full_name'])
        address_1 = html_escape(request.POST['address_1'])
        address_2 = html_escape(request.POST['address_2'])
        city_name = html_escape(request.POST['city_name'])
        state = html_escape(request.POST['state'])
        zip_code = html_escape(request.POST['zip_code'])

        # Validate input
        if state not in states:
            pass  # Do something

        # Update or create the user's profile entry
        user_profile, created = ProfileInfo.objects.update_or_create(
            user_id=request.user.id,
            defaults={
                'full_name': full_name,
                'address_line_1': address_1,
                'address_line_2': address_2,
                'city_name': city_name,
                'state': state,
                'zip_code': zip_code
            }
        )

        # Populate the form with the entered values
        context["full_name"] = full_name
        context["address_1"] = address_1
        context["address_2"] = address_2
        context["city_name"] = city_name
        context["state"] = state
        context["zip_code"] = zip_code

        context["profile_updated"] = True
        context["msg_profile_updated"] = msg_profile_updated

    else:
        if "order_needs_profile" in request.GET:
            # Display helpful prompt if user must complete their profile
            context["incomplete_profile"] = True
            context["msg_update_profile"] = msg_update_profile

        try:
            user_profile = ProfileInfo.objects.get(user_id=request.user.id)

            # Populate the form with the existing values
            context["full_name"] = user_profile.full_name
            context["address_1"] = user_profile.address_line_1
            context["address_2"] = user_profile.address_line_2
            context["city_name"] = user_profile.city_name
            context["state"] = user_profile.state
            context["zip_code"] = user_profile.zip_code
        except ProfileInfo.DoesNotExist:
            pass

    return render(request, 'FuelProjectDev/profile.html', context,
                  content_type='text/html')

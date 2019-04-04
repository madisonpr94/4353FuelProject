from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

from .forms.quote_form import QuoteForm
from .pricing import get_price
from ..models.profile_info import ProfileInfo
from ..models.past_order import PastOrder

msg_submit_success = "Purchase successful!"


# Redirect if user not logged in
@login_required
def quote_page(request):
    context = {}

    context["msg_submit_success"] = msg_submit_success

    # Check for form POST data
    if request.method == 'POST':
        context["form_submitted"] = True

        form = QuoteForm(request.POST)  # Form validation

        gallons = float(form['gallons'].value())
        date = datetime.strptime(form['delivery_date'].value(), "%Y-%m-%d")

        if form.is_valid():
            context["order_success"] = True

            # Fetch profile info
            try:
                profile = ProfileInfo.objects.get(user_id=request.user.id)
                past_orders = len(
                    PastOrder.objects.filter(user_id=request.user.id)
                )
            except ProfileInfo.DoesNotExist:
                return HttpResponse(None, status='500')

            # Format address for order history
            full_address = (profile.address_line_1 + " " +
                            (profile.address_line_2 + " "
                                if profile.address_line_2 != "" else "") +
                            profile.city_name + ", " + profile.state +
                            " " + profile.zip_code)

            if len(full_address) >= 50:
                full_address = full_address[:47] + "..."

            # Fetch price info: Do not trust submitted form!
            prices = get_price(gallons, date, profile, past_orders)

            # Add order to user's order history
            PastOrder.objects.create(
                user_id=request.user.id,
                gallons=gallons,
                delivery_addr=full_address,
                delivery_date=date,
                unit_price=prices[0],
                total_price=prices[1]
            )
        else:
            context["form"] = form

    # == Continue to render page ==

    # Default form values
    context['gallons'] = 10

    delivery_date = datetime.now() + timedelta(days=2)
    context['delivery_date'] = delivery_date

    # Overwrite defaults if form data exists
    if 'form' in context:
        context['gallons'] = context['form']['gallons'].value()
        context['delivery_date'] = datetime.strptime(
            context['form']['delivery_date'].value(), "%Y-%m-%d")

    # Fetch user account info
    user_id = request.user.id
    try:
        user_profile = ProfileInfo.objects.get(user_id=user_id)
        context['user_addr_line1'] = user_profile.address_line_1
        context['user_addr_line2'] = user_profile.address_line_2
        context['user_addr_city'] = user_profile.city_name
        context['user_addr_state'] = user_profile.state
        context['user_addr_zip'] = user_profile.zip_code
    except ProfileInfo.DoesNotExist:
        # If user has not completed their profile, redirect them with a prompt
        return HttpResponseRedirect("/profile?order_needs_profile")

    return render(request, 'FuelProjectDev/quote_request.html', context,
                  content_type='text/html')

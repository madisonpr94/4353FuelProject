from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from datetime import datetime, timedelta

from .util import *
from .forms.quote_form import QuoteForm


def quote_page(request):
    # Redirect if user not logged in
    # Disabled until login implemented
    """if not request.user.is_authenticated:
        return redirect_with_GET('login_page',
                                 kwargs={"redirect_not_logged_in": True})"""

    context = {}

    # Check for form POST data
    if request.method == 'POST':
        context["form_submitted"] = True

        form = QuoteForm(request.POST)  # Form validation

        gallons = form['gallons'].value()
        date = form['delivery_date'].value()

        if form.is_valid():
            context["order_success"] = True
            # To Do: Add order history to user account (Assignment 4)

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

    # Placeholder account info - Replace by database entry in Assignment 4
    context['user_addr_line1'] = "123 Example St."
    context['user_addr_line2'] = ""
    context['user_addr_city'] = "Spring"
    context['user_addr_state'] = "Texas"
    context['user_addr_zip'] = "77383"

    # User account info
    context['username'] = request.user.username

    return render(request, 'FuelProjectDev/quote_request.html', context,
                  content_type='text/html')

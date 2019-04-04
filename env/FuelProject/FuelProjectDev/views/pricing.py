from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
import json

from ..models.profile_info import ProfileInfo
from ..models.past_order import PastOrder


def get_price(gallons, date, user_profile, past_orders):
    # Price calculation:
    base_price = 1.50

    state = user_profile.state
    loc_factor = 0.02 if state == "Texas" else 0.04
    rate_history_factor = 0.01 if past_orders > 0 else 0.00
    gallons_requested_factor = 0.02 if gallons >= 1000 else 0.03
    company_profit_factor = 0.10  # Fixed
    rate_fluctuation = 0.04 if date.month in range(6, 9) else 0.03

    margin = (base_price) * (loc_factor - rate_history_factor +
                             gallons_requested_factor + company_profit_factor +
                             rate_fluctuation)

    price_per_gallon = base_price + margin
    total_price = price_per_gallon * gallons

    return (price_per_gallon, total_price)


@login_required
def price_module(request):
    # Verify all GET arguments have been provided
    if not all(x in request.GET for x in ['gallons', 'date']):
        return HttpResponse(None, status='400')

    gallons = float(request.GET["gallons"])
    delivery_date = datetime.strptime(request.GET["date"], "%Y-%m-%d")

    # Verify the date is acceptable
    delta = delivery_date - datetime.today()
    if delta.days < 1:
        return HttpResponse(None, status='400')

    # Retrieve user information
    try:
        user_profile = ProfileInfo.objects.get(user_id=request.user.id)
        past_orders = len(PastOrder.objects.filter(user_id=request.user.id))
    except ProfileInfo.DoesNotExist:
        return HttpResponse(None, status='400')

    result = get_price(gallons, delivery_date, user_profile, past_orders)

    price = {
        'gallons_requested': gallons,
        'price_per_gallon': result[0],
        'total_price': result[1]
    }
    data = json.dumps(price)

    return HttpResponse(data, content_type='application/json')

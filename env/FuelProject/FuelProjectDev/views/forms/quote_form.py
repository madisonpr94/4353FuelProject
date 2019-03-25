from django import forms

from ..util import *


class QuoteForm(forms.Form):
    gallons = forms.FloatField(min_value=10, max_value=1000000)
    delivery_date = forms.DateField()

from django.contrib.auth import get_user_model
from django.db import models


class ProfileInfo(models.Model):
    # FOREIGN KEY PRIMARY KEY User
    # STRING Full Name
    # STRING Address Line 1
    # STRING Address Line 2
    # STRING City Name
    # STRING State
    # INT ZIP Code

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True
    )

    full_name = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, null=True)
    city_name = models.CharField(max_length=100)
    state = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=10)

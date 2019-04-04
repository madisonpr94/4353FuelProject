from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse
import re

from ..views.pricing import price_module
from ..models.profile_info import ProfileInfo


class PricingTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test_user',
                                             email=None, password='secret')

        self.user_profile = ProfileInfo.objects.create(
            user_id=self.user.id,
            full_name="Test User",
            address_line_1="123 Example St.",
            address_line_2="",
            city_name="Mobile",
            state="Alabama",
            zip_code="12345"
        )

    def test_returns200IfAuth(self):
        request = self.factory.get('/price_module?gallons=20&date=2020-12-31')
        request.user = self.user

        response = price_module(request)

        self.assertEqual(response.status_code, 200)

    def test_returns302IfUnauth(self):
        request = self.factory.get('/price_module?gallons=20&date=2020-12-31')
        request.user = AnonymousUser()

        response = price_module(request)

        self.assertEqual(response.status_code, 302)

    def test_responseIsJSON(self):
        request = self.factory.get('/price_module?gallons=20&date=2020-12-31')
        request.user = self.user

        response = price_module(request)

        self.assertTrue("application/json" in response['Content-Type'])

    def test_returns400IfNoDate(self):
        request = self.factory.get('/price_module?gallons=20')
        request.user = self.user

        response = price_module(request)

        self.assertEqual(response.status_code, 400)

    def test_returns400IfNoGallons(self):
        request = self.factory.get('/price_module?date=2020-12-31')
        request.user = self.user

        response = price_module(request)

        self.assertEqual(response.status_code, 400)

    def test_returns400IfBadDate(self):
        request = self.factory.get('/price_module?gallons=20&date=1970-1-1')
        request.user = self.user

        response = price_module(request)

        self.assertEqual(response.status_code, 400)

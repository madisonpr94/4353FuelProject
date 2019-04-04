from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse
import re
from datetime import datetime

from ..views.history import history_page
from ..models.profile_info import ProfileInfo
from ..models.past_order import PastOrder


class HistoryTest(TestCase):
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
        self.past_order = PastOrder.objects.create(
            user_id=self.user.id,
            gallons=500,
            delivery_addr="123 Example St. Mobile, Alabama 12345",
            delivery_date=datetime.strptime("2019-07-23", "%Y-%m-%d"),
            unit_price=1.00,
            total_price=500.00
        )

    def test_returns200IfAuth(self):
        request = self.factory.get('/order_history')
        request.user = self.user

        response = history_page(request)

        self.assertEqual(response.status_code, 200)

    def test_returns302IfUnauth(self):
        request = self.factory.get('/order_history')
        request.user = AnonymousUser()

        response = history_page(request)

        self.assertEqual(response.status_code, 302)

    def test_responseIsHTML(self):
        request = self.factory.get('/order_history')
        request.user = self.user

        response = history_page(request)

        self.assertTrue("text/html" in response['Content-Type'])

    def test_tableHasRows(self):
        request = self.factory.get('/order_history')
        request.user = self.user

        response = history_page(request)

        self.assertGreaterEqual(response.content.count(b"<tr>"), 2)

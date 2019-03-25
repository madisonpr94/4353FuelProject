from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse
import re

from ..views.history import history_page


class HistoryTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test_user',
                                             email=None, password='secret')

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

        self.assertGreater(response.content.count(b"<tr>"), 2)

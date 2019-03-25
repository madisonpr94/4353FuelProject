from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client
from datetime import datetime

from ..views.quote import quote_page, msg_submit_success


class QuoteTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user('test_user',
                                             None,
                                             'secret')
        self.user.save()

        self.client.login(username='test_user', password='secret')

    def test_returns200IfAuth(self):
        request = self.factory.get("/quote_request")
        request.user = self.user

        response = quote_page(request)

        self.assertEquals(response.status_code, 200)

    def test_returns302IfNotAuth(self):
        request = self.factory.get("/quote_request")
        request.user = AnonymousUser()

        response = quote_page(request)

        self.assertEquals(response.status_code, 302)

    def test_formSubmitSuccess(self):
        response = self.client.post("/quote_request", {
                            "gallons": "500",
                            "delivery_date": "2019-12-31"
                            })

        content = response.content.decode(response.charset)

        self.assertEquals(response.status_code, 200)
        self.assertTrue(msg_submit_success in content)

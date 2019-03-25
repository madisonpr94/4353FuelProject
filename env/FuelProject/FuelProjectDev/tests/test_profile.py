from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client

from ..views.profile import *


class ProfileTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user('test_user',
                                             None,
                                             'secret')
        self.user.save()

        self.client.login(username='test_user', password='secret')

    def test_returns200IfAuth(self):
        request = self.factory.get("/profile")
        request.user = self.user

        response = profile_page(request)

        self.assertEquals(response.status_code, 200)

    def test_returns302IfNotAuth(self):
        request = self.factory.get("/profile")
        request.user = AnonymousUser()

        response = profile_page(request)

        self.assertEquals(response.status_code, 302)

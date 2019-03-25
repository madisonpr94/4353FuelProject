from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse
import re

from ..views.index import index_page


class IndexTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test_user',
                                             email=None, password='secret')

    def test_returns200(self):
        request = self.factory.get('/')
        request.user = self.user

        response = index_page(request)

        self.assertEqual(response.status_code, 200)

        request.user = AnonymousUser()  # Simulate a user who is not logged in
        response = index_page(request)

        self.assertEqual(response.status_code, 200)

    def test_responseIsHTML(self):
        request = self.factory.get('/')
        request.user = self.user

        response = index_page(request)

        self.assertTrue("text/html" in response['Content-Type'])

    def test_hasLoginButtonIfNoAuth(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()

        response = index_page(request)

        desiredHTML = """<a class="nav-item nav-link" href=\"""" + \
            reverse('login_page') + """\">Log In</a>"""
        self.assertTrue(desiredHTML in response.content.decode(response.charset))

    def test_hasLogoutButtonIfAuth(self):
        request = self.factory.get('/')
        request.user = self.user

        response = index_page(request)

        desiredHTML = """<a class="nav-item nav-link" href=\"""" + \
            reverse('logout_page') + """\">Log Out</a>"""
        self.assertTrue(desiredHTML in response.content.decode(response.charset))

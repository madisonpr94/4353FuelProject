from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
import re

from ..views.login import *


class LoginTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='test_user',
                                             email=None, password='secret')

    def test_returns200(self):
        request = self.factory.get('/login')
        request.user = self.user
        response = login_page(request)

        self.assertEqual(response.status_code, 200)

        request.user = AnonymousUser()
        response = login_page(request)

        self.assertEqual(response.status_code, 200)

    def test_responseIsHTML(self):
        request = self.factory.get('/login')
        request.user = self.user
        response = login_page(request)

        self.assertTrue("text/html" in response['Content-Type'])

    def test_loginWithValidCredentials(self):
        response = self.client.post("/login", {
            "username": "test_user",
            "password": "secret"
        })

        content = response.content.decode(response.charset)

        self.assertTrue(response.status_code, 302)

    def test_loginWithInvalidCredentials(self):
        response = self.client.post("/login", {
            "username": "test_user",
            "password": "wrong"
        })

        content = response.content.decode(response.charset)

        self.assertTrue(response.status_code, 200)
        self.assertTrue(msg_login_error in content)

    def test_validRegister(self):
        response = self.client.post("/login", {
            "username-register": "new_user",
            "password-register": "secret2",
            "password-confirm": "secret2"
        })

        content = response.content.decode(response.charset)

        self.assertTrue(response.status_code, 200)
        self.assertTrue(msg_register_success in content)

        response = self.client.post("/login", {
            "username": "new_user",
            "password": "secret2"
        })

        self.assertTrue(response.status_code, 302)

    def test_registerBadName(self):
        response = self.client.post("/login", {
            "username-register": "test_user",
            "password-register": "secret3",
            "password-confirm": "secret3"
        })

        content = response.content.decode(response.charset)

        self.assertTrue(response.status_code, 200)
        self.assertTrue(msg_username_unavail in content)

    def test_registerPasswordMismatch(self):
        response = self.client.post("/login", {
            "username-register": "test_user",
            "password-register": "secret3",
            "password-confirm": "wrong3"
        })

        content = response.content.decode(response.charset)

        self.assertTrue(response.status_code, 200)
        self.assertTrue(msg_password_mismatch in content)

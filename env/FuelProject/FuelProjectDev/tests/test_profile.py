from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client

from ..views.profile import *
from ..models.profile_info import ProfileInfo


class ProfileTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user('test_user',
                                             None,
                                             'secret')
        self.user.save()

        self.user_profile = ProfileInfo.objects.create(
            user_id=self.user.id,
            full_name="Test User",
            address_line_1="123 Example St.",
            address_line_2="",
            city_name="Mobile",
            state="Alabama",
            zip_code="12345"
        )

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

    def test_submitProfile(self):
        response = self.client.post("/profile", {
            "full_name": "Gary Smith",
            "address_1": "4392 Post Oak Avenue",
            "address_2": "",
            "city_name": "Houston",
            "state": "Texas",
            "zip_code": "77503",
        })

        content = response.content.decode(response.charset)

        self.assertEqual(response.status_code, 200)
        self.assertInHTML("<option selected>Texas</option>", content)

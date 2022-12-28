from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from ilara.backoffice.models import UserProfile


class BaseTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user_creds = {
            "username": "jdoe",
            "email": "jdoe@example.com",
            "password": "jdoe123",
        }
        self.user = User.objects.create_user(**self.user_creds)
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            birthday=datetime.today(),
            gender=1,
            phone="+123456789",
            address="Nowhere, Middle Of.",
        )

    def tearDown(self) -> None:
        return super().tearDown()


class GetUserViewTestCase(BaseTest):
    def setUp(self) -> None:
        self.url = reverse("get_user")
        return super().setUp()

    def test_get_user(self):
        self.client.login(
            username=self.user_creds["username"], password=self.user_creds["password"]
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            self.user_profile.address, response.json()["user"][0]["address"]
        )

    def test_get_unauthenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class AuthViewTestCase(BaseTest):
    def setUp(self) -> None:
        self.url = reverse("login")
        return super().setUp()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post(self.url, data=self.user_creds)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_incorrect_credentials(self):
        response = self.client.post(
            self.url, data=dict(username="John", password="doe")
        )
        self.assertEqual(response.status_code, 403)
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class CreateAnonymousUserViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("create_anon_user")

    def test_create_anonymous_user(self):
        self.assertEqual(0, User.objects.all().count())
        response = self.client.post(self.url)
        self.assertEqual(response.wsgi_request.user, User.objects.first())
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertFalse(response.wsgi_request.user.is_staff)


class LogoutViewTestCase(BaseTest):
    def setUp(self) -> None:
        self.url = reverse("logout")
        return super().setUp()

    def test_logout(self):
        self.client.login(
            username=self.user_creds["username"], password=self.user_creds["password"]
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

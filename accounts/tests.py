from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.


class AccountTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username="ata", password="1234")
        self.token = None
        return super().setUp()

    def test_register(self):
        data = {
            "first_name": "ata",
            "last_name": "attarian",
            "email": "ata.attarian78@gmail.com",
            "username": "ataattarian",
            "password": "12345678",
            "confirm_password": "12345678",
        }
        request = self.client.post("/api/accounts/register", data)
        self.assertEquals(request.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        data = {"username": "ata", "password": "1234"}
        request = self.client.post("/api/accounts/login/", data)
        self.token = request.json().get("access")
        self.assertEquals(request.status_code, status.HTTP_200_OK)

    def test_get_profile(self):
        self.test_login()
        request = self.client.get(
            "/api/accounts/profile", HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEquals(request.status_code, status.HTTP_200_OK)

    def test_update_profile(self):
        self.test_login()
        data = {"first_name": "ata", "last_name": "attarian"}
        request = self.client.patch(
            "/api/accounts/profile", data, HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEquals(request.status_code, status.HTTP_200_OK)

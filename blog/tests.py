from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.


class BlogTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username="ata", password="1234")
        data = {"username": "ata", "password": "1234"}
        request = self.client.post("/api/accounts/login/", data)
        self.token = request.json().get("access")
        return super().setUp()

    def test_get_blog(self):
        request = self.client.get("/api/blogs/")
        self.assertEquals(request.status_code, status.HTTP_200_OK)

    def test_create_blog(self):
        data = {"title": "Test", "content": "test content"}
        request = self.client.post(
            "/api/blogs/", data, HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.blog_id = request.json().get("id")
        self.assertEquals(request.status_code, status.HTTP_201_CREATED)

    def test_update_blog(self):
        self.test_create_blog()
        data = {"title": "TestUpdate", "content": "test update content"}
        request = self.client.patch(
            f"/api/blogs/{self.blog_id}/",
            data,
            HTTP_AUTHORIZATION=f"Bearer {self.token}",
        )
        self.assertEquals(request.status_code, status.HTTP_200_OK)

    def test_rate_blog(self):
        self.test_create_blog()
        data = {"blog": self.blog_id, "rate": 5}
        request = self.client.post(
            "/api/blogs/rate", data, HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEquals(request.status_code, status.HTTP_201_CREATED)

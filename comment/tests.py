from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from blog.models import BlogModel

# Create your tests here.


class CommentTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="ata", password="1234")
        blog = BlogModel.objects.create(
            title="TestBlog", content="test content", author=user
        )
        self.blog_id = blog.id
        data = {"username": "ata", "password": "1234"}
        request = self.client.post("/api/accounts/login/", data)
        self.token = request.json().get("access")
        return super().setUp()

    def test_comment(self):
        data = {"content": "TestComment", "blog": self.blog_id}
        request = self.client.post(
            "/api/comments/", data, HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.comment_id = request.json().get("id")
        self.assertEquals(request.status_code, status.HTTP_201_CREATED)

    def test_update_comment(self):
        self.test_comment()
        data = {"content": "Test Update Comment"}
        request = self.client.patch(
            f"/api/comments/{self.comment_id}/",
            data,
            HTTP_AUTHORIZATION=f"Bearer {self.token}",
        )
        self.assertEquals(request.status_code, status.HTTP_200_OK)

    def test_destroyed_comment(self):
        self.test_comment()
        request = self.client.delete(
            f"/api/comments/{self.comment_id}/",
            HTTP_AUTHORIZATION=f"Bearer {self.token}",
        )
        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)

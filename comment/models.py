from django.db import models
from django.contrib.auth.models import User
from blog.models import BlogModel

# Create your models here.


class CommentModel(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_comments",
        null=True,
        blank=True,
    )
    content = models.CharField(max_length=1000)
    publication_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(
        BlogModel,
        on_delete=models.CASCADE,
        related_name="comments",
    )

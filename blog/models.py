from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blogs",
    )
    publication_date = models.DateTimeField(auto_now_add=True)


class RateModel(models.Model):
    rate = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    ip = models.CharField(max_length=15)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_rates", null=True, blank=True
    )
    blog = models.ForeignKey(
        BlogModel,
        on_delete=models.CASCADE,
        related_name="blog_rates",
    )

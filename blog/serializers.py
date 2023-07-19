from rest_framework import serializers
from blog.models import BlogModel
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = BlogModel
        fields = ("id", "title", "content", "publication_date", "author")
        extra_kwargs = {
            "author": {"read_only": True},
            "publication_date": {"read_only": True},
        }

    def create(self, validated_data):
        blog = BlogModel.objects.create(
            title=validated_data["title"],
            content=validated_data["content"],
            author=self.context["request"].user,
        )
        return blog

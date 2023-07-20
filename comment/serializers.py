from rest_framework import serializers
from comment.models import CommentModel
from django.contrib.auth.models import User


class CommentAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class CommentSerializer(serializers.ModelSerializer):
    author = CommentAuthorSerializer(required=False)

    class Meta:
        model = CommentModel
        fields = ("id", "content", "blog", "author", "publication_date")
        extra_kwargs = {
            "author": {"read_only": True},
            "publication_date": {"read_only": True},
        }

    def create(self, validated_data):
        request = self.context["request"]
        comment = CommentModel.objects.create(
            content=validated_data["content"],
            blog=validated_data["blog"],
            author=request.user if request.user.is_authenticated else None,
        )
        return comment

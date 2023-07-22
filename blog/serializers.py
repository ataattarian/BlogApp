from rest_framework import serializers
from blog.models import BlogModel, RateModel
from django.contrib.auth.models import User
from comment.serializers import CommentSerializer
from django.db.models import Avg


def get_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateModel
        fields = ("id", "ip", "user", "blog", "rate")
        extra_kwargs = {
            "ip": {"read_only": True},
            "user": {"read_only": True},
        }

    def validate(self, attrs):
        request = self.context["request"]
        ip = get_ip(request=request)
        check_ip = RateModel.objects.filter(ip=ip, blog_id=attrs["blog"])
        error = 0
        if request.user.is_authenticated:
            check_user = RateModel.objects.filter(
                user=request.user, blog_id=attrs["blog"]
            )
            if check_user:
                error = 1
            elif check_ip:
                error = 1
        else:
            if check_ip:
                error = 1
        if error:
            raise serializers.ValidationError("You rated this blog")
        return attrs

    def create(self, validated_data):
        request = self.context["request"]
        ip = get_ip(request=request)
        rate = RateModel.objects.create(
            ip=ip,
            user=request.user if request.user.is_authenticated else None,
            blog=validated_data["blog"],
            rate=validated_data["rate"],
        )
        return rate


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    rate = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = BlogModel
        fields = (
            "id",
            "title",
            "content",
            "publication_date",
            "author",
            "rate",
            "comments",
        )
        extra_kwargs = {
            "author": {"read_only": True},
            "publication_date": {"read_only": True},
            "rate": {"read_only": True},
            "comments": {"read_only": True},
        }

    def get_rate(self, obj):
        rate = obj.blog_rates.aggregate(Avg("rate"))
        return rate["rate__avg"] if rate["rate__avg"] else 0

    def get_comments(self, obj):
        comments = CommentSerializer(obj.comments.all(), many=True)
        return comments.data

    def create(self, validated_data):
        blog = BlogModel.objects.create(
            title=validated_data["title"],
            content=validated_data["content"],
            author=self.context["request"].user,
        )
        return blog

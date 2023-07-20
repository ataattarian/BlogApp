from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from comment.models import CommentModel
from comment.serializers import CommentSerializer
from django.db.models import Q

# Create your views here.


class CommentView(
    CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet
):
    model = CommentModel
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return CommentModel.objects.filter(
                Q(author=self.request.user) | Q(blog__author=self.request.user)
            )
        else:
            return None

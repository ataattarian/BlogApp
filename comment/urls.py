from django.urls import path
from rest_framework import routers
from comment.views import CommentView

router = routers.DefaultRouter()
router.register("", CommentView, basename="comment")

urlpatterns = [] + router.urls

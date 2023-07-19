from django.urls import path
from rest_framework import routers
from blog.views import BlogView, RateView

router = routers.DefaultRouter()
router.register("", BlogView, basename="blogs")

urlpatterns = [
    path("rate", RateView.as_view(), name="rate"),
] + router.urls

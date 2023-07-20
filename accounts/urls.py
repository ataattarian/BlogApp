from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from accounts.views import RegisterView, ProfileView


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register", RegisterView.as_view(), name="register"),
    path("profile", ProfileView.as_view(), name="profile"),
]

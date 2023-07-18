from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from accounts.views import RegisterView, ProfileView


urlpatterns = [
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register", RegisterView.as_view(), name="register"),
    path("api/profile", ProfileView.as_view(), name="profile"),
]

from django.shortcuts import render
from rest_framework import generics
from accounts.serializers import RegisterSerializer
from django.contrib.auth.models import User

# Create your views here.


class RegisterView(generics.CreateAPIView):
    model = User
    serializer_class = RegisterSerializer

from rest_framework import generics
from accounts.serializers import RegisterSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class RegisterView(generics.CreateAPIView):
    model = User
    serializer_class = RegisterSerializer


class ProfileView(generics.RetrieveAPIView, generics.UpdateAPIView):
    model = User
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

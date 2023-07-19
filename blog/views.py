from rest_framework import viewsets
from blog.serializers import BlogSerializer
from blog.models import BlogModel
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class BlogView(viewsets.ModelViewSet):
    model = BlogModel
    serializer_class = BlogSerializer

    def get_permissions(self):
        if not self.request.method == "GET":
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_queryset(self):
        if self.request.method == "GET":
            return BlogModel.objects.all()
        else:
            return BlogModel.objects.filter(author=self.request.user)

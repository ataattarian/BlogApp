from rest_framework import routers
from blog.views import BlogView

router = routers.DefaultRouter()
router.register("", BlogView, basename="blogs")

urlpatterns = [] + router.urls

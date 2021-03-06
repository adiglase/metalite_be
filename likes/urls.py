from django.urls import path, include
from rest_framework.routers import DefaultRouter

from likes.views import LikeViewSet

router = DefaultRouter()
router.register("likes", LikeViewSet, basename="likes")

urlpatterns = [
    path('', include(router.urls))
]

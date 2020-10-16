from rest_framework import routers
from django.urls import path, include
from .views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'', ProjectViewSet, basename='Project Management')

urlpatterns = [
    path("", include(router.urls))
]

from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='User Management')

urlpatterns = [
    path('', include(router.urls))
]

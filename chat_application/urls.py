from rest_framework import routers
from django.urls import path, include
from .views import ChatApplicationViewset

router = routers.DefaultRouter()
router.register(r'', ChatApplicationViewset, basename='Chat Application')

urlpatterns = [
    path("", include(router.urls))
]

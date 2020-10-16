from rest_framework import routers
from django.urls import path, include
from .views import DailyUpdatesViewsets

router = routers.DefaultRouter()
router.register(r'', DailyUpdatesViewsets, basename='Chat Application')

urlpatterns = [
    path("", include(router.urls))
]

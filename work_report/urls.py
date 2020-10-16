from django.urls import path, include
from rest_framework import routers
from .views import ReportViewSet

router = routers.DefaultRouter()
router.register(r'', ReportViewSet, basename='Work Report')

urlpatterns = [
    path('', include(router.urls))
]

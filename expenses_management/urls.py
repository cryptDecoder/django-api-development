from rest_framework import routers
from django.urls import path, include
from .views import ExpenseseViewSet

router = routers.DefaultRouter()
router.register(r'', ExpenseseViewSet, basename='Expense Management')

urlpatterns = [
    path("", include(router.urls))
]

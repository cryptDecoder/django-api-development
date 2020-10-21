from rest_framework import routers
from django.urls import path, include
from .views import ExpensesViewSet, ExpensesDetailViewSet

urlpatterns = [
    path('', ExpensesViewSet.as_view(), name='Expenses'),
    path('<int:id>', ExpensesDetailViewSet.as_view(), name="expense")
]

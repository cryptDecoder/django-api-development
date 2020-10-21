from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpenseSerializer
from .models import Expense
from rest_framework import permissions
from .permissions import IsOwner


class ExpensesViewSet(ListCreateAPIView):
    @classmethod
    def get_extra_actions(cls):
        return []

    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpensesDetailViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save(owner=self.request)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

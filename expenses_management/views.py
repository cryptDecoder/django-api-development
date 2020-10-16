from django.http import JsonResponse
from rest_framework import viewsets


class ExpenseseViewSet(viewsets.ModelViewSet):
    def list(self, request):
        return JsonResponse({'Hello': 'This is Expense Management API'})

        pass

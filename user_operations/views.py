from django.http import JsonResponse
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    def list(self, request):
        return JsonResponse({'Hello': "Welcome to User API"})

from django.http import JsonResponse
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    def list(self, request):
        return JsonResponse({'Hello': "Welcome to Task API"})

        pass

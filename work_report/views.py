from django.http import JsonResponse
from rest_framework import viewsets


class ReportViewSet(viewsets.ModelViewSet):
    def list(self, request):
        return JsonResponse({"Hello": "This is Report API"})

        pass

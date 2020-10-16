from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets


class DailyUpdatesViewsets(viewsets.ModelViewSet):
    def list(self, request):
        return JsonResponse({'Hello': 'This is daily updates'})
        pass

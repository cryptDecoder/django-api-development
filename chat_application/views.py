from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse


class ChatApplicationViewset(viewsets.GenericViewSet):
    """Created Chat application API"""

    def list(self, request):
        """Return welcome to Chat application"""
        a_list = [
            'user_actions',
            'Recive Messages',
            'send Messges'
        ]
        return JsonResponse({'hello': 'Welcome to Chat application', 'a_list': a_list})

    pass

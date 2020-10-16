from django.http import JsonResponse
from rest_framework import viewsets


class ProjectViewSet(viewsets.ModelViewSet):

    def list(self, request):
        """Return welcome to Chat application"""
        a_list = [
            'user_actions',
            'Create Projects',
            'Manage Projects'
        ]
        return JsonResponse({'hello': 'Welcome to Project', 'a_list': a_list})

        pass

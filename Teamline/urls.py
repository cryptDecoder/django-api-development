"""Teamline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
    openapi.Info(
        title="Teamline API",
        default_version='v1',
        description="This API build by pruthviraj for use of Taeamline project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@teamline.local"),
        license=openapi.License(name="teamline License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat_application.urls'), name="Chat Application"),
    path('daily-updates/', include('daily_updates.urls'), name="Daily Updates"),
    path('expenses/', include('expenses_management.urls'), name="Expenses Management"),
    path('projects/', include('project_management.urls'), name="Project Management"),
    path('tasks/', include('task_management.urls'), name="Task Management"),
    path('report/', include('work_report.urls'), name='Work Report'),
    path('auth/', include('accounts.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

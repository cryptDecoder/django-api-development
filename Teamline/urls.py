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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat_application.urls'), name="Chat Application"),
    path('daily-updates/', include('daily_updates.urls'), name="Daily Updates"),
    path('expenses/', include('expenses_management.urls'), name="Expenses Management"),
    path('projects/', include('project_management.urls'), name="Project Management"),
    path('tasks/', include('task_management.urls'), name="Task Management"),
    path('users/', include('user_operations.urls'), name="User Management"),
    path('report/', include('work_report.urls'), name='Work Report')

]

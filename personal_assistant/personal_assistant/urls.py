"""
URL configuration for personal_assistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# Adjust the import statement here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_assistant.urls')),
    path('app_contacts/', include('app_contacts.urls')),
    path('app_notes/', include('app_notes.urls')),
    path("users/", include("users.urls")),
    path('app_news/', include('app_news.urls')),
]

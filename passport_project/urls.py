"""passport_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import login
from django.urls import path, include, reverse_lazy
from home import views as home_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_views.user_login, name='user_login'),
    path('', RedirectView.as_view(url=reverse_lazy('home:index')), name='index'),
    path('accounts/', include('allauth.urls')),
    path('home/', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('courses/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('schedules/', include('schedules.urls')),
    path('wiawdp/', include('wiawdp.urls')),
    path('billing/', include('billing.urls')),
    # Add URL maps to redirect the base URL to the given application
]

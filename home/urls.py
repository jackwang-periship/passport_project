# Use include() to add paths from the home application
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'), # New mapping!
    path('userprofiles/', views.UserProfileListView.as_view(), name='list_userprofiles'),
    path('userprofile/(?P<pk>[0-9]+)/$', views.UserProfileDetailView.as_view(), name='userprofile-detail'),
]

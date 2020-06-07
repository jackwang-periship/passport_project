# Use include() to add paths from the home application
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'), # New mapping!
    path('employees/', views.EmployeeListView.as_view(), name='employees'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
]
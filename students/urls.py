# Use include() to add paths from the home application
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('studentlist/', views.StudentListView.as_view(), name='student_list'),
]
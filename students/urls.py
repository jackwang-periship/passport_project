# Use include() to add paths from the home application
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('studentlist/', views.StudentListView.as_view(), name='student_list'),
    path('add_new_student/', views.AddStudentView.as_view(), name='add_new_student'),
    path('current_student/', views.CurrentStudentView.as_view(), name='current_student'),
    path('help_setting/', views.HelpSettingView.as_view(), name='help_setting'),
    path('student_home/', views.StudentHomeView.as_view(), name='student_Home'),
    path('change_password/', views.StudentPasswordView.as_view(), name='change_password'),
    path('public_student/', views.PublicStudentView.as_view(), name='public_student'),
    path('search_student/', views.SearchStudentView.as_view(), name='search_student'),
]
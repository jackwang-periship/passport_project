# Use include() to add paths from the home application
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('studentlist/', views.StudentListView.as_view(), name='student_list'),
    path('add_new_student/', views.AddStudentView.as_view(), name='add_new_student'),
    path('student_home/', views.StudentHomeView.as_view(), name='student_Home'),
    path('search_student/', views.SearchStudentView.as_view(), name='search_student'),
    path('delete_student/', views.DeleteStudentView.as_view(), name='delete_student'),
    path('modify_student/', views.ModifyStudentView.as_view(), name='modify_student'),
    path('modify_student_lookup/', views.ModifyStudentLookUpView.as_view(), name='modify_student_lookup'),
]
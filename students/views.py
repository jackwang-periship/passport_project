from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from students.forms import StudentForm, SearchStudentForm, ChangePasswordForm
from datetime import datetime
from django.shortcuts import reverse

from .models import Student

class StudentListView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_list'
    queryset = Student.objects.filter
    template_name = 'students/student_list.html'
    permission_required = 'students.can_list_students'

    def get_queryset(self):
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context["sidebar_data"] = 'This holds the sidebar data for students'
        return context

class AddStudentView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'students/add_new_student.html'
    permission_required = 'students.addStudents'
    form_class = StudentForm

class CurrentStudentView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'students/current_student.html'
    permission_required = 'students.view_current_Students'

    def get_queryset(self):
        return Student.objects.all()

class HelpSettingView():
    template_name = 'students/help_setting.html'

class StudentHomeView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'students/StudentHomeView.html'
    permission_required = 'students.home'

class StudentPasswordView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'students/change_password.html'
    permission_required = 'students.changePassword'
    form_class = ChangePasswordForm

class PublicStudentView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'students/public_student.html'
    permission_required = 'students.viewPublic'

    def get_queryset(self):
        return Student.objects.all()


class SearchStudentView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'students/search_student.html'
    permission_required = 'students.search'
    form_class = SearchStudentForm

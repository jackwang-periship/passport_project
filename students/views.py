from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from students.forms import StudentForm, SearchStudentForm, ChangePasswordForm
from datetime import datetime
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Student

class StudentListView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_list'
    queryset = Student.objects.filter
    template_name = 'students/student_list.html'

    def get_queryset(self):
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context["sidebar_data"] = 'This holds the sidebar data for students'
        return context

class AddStudentView(PermissionRequiredMixin, generic.CreateView):
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

class HelpSettingView(generic.ListView):
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

class SearchStudentView(PermissionRequiredMixin, generic.FormView):
    context_object_name = 'student_list'
    template_name = 'students/search_student.html'
    permission_required = 'students.search'
    form_class = SearchStudentForm

    def form_valid(self, form):
        student_list = Student.objects
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        ID = form.cleaned_data['ID']
        phone = form.cleaned_data['phone']

        if not any((first_name, last_name, ID, phone)):
            return render(self.request, 'students/search_student_result.html',
                          context={'active_student_list': []})

        if first_name:
            student_list = student_list.filter(student__first_name__iexact=first_name)
        if last_name:
            student_list = student_list.filter(student__last_name__iexact=last_name)
        if ID:
            student_list = student_list.filter(student__ID__iexact=ID)
        if phone:
            student_list = student_list.filter(student__phone__iexact=phone)
        return render(self.request, 'students/search_student_result.html',
                      context={'active_student_list': student_list})

class DeleteStudentView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('student:student_list')

    def get_object(self, queryset=None):
        return Student.objects.get(pk=self.request.GET.get('pk'))
from typing import Any, Union

from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from students.forms import StudentForm, SearchStudentForm, ChangePasswordForm, ModifyStudentForm
from django.urls import reverse_lazy
from django.shortcuts import render
from students.tables import StudentTable
from .models import Student


class StudentListView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_list'
    queryset = Student.objects.filter
    template_name = 'students/student_list.html'
    permission_required = 'students.viewStudents'

    def get_queryset(self):
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context["sidebar_data"] = 'This holds the sidebar data for students'
        return context


class AddStudentView(PermissionRequiredMixin, generic.CreateView):
    model = Student
    context_object_name = 'add_student'
    template_name = 'students/add_new_student.html'
    permission_required = 'students.addStudents'
    form_class = StudentForm
    success_url = reverse_lazy("student:student_list")


class StudentHomeView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_home'
    template_name = 'students/StudentHomeView.html'
    permission_required = 'students.home'


class StudentPasswordView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_password'
    template_name = 'students/change_password.html'
    permission_required = 'students.changePassword'
    form_class = ChangePasswordForm


class SearchStudentView(PermissionRequiredMixin, generic.FormView):
    context_object_name = 'search_student'
    template_name = 'students/search_student.html'
    permission_required = 'students.search'
    form_class = SearchStudentForm

    def form_valid(self, form):
        student_list = Student.objects
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        RecId = form.cleaned_data['id']

        if not any((first_name, last_name, RecId)):
            return render(self.request, 'students/search_student_result.html',
                          context={'active_student_list': []})

        if first_name:
            student_list = student_list.filter(student__first_name__iexact=first_name)
        if last_name:
            student_list = student_list.filter(student__last_name__iexact=last_name)
        if RecId:
            student_list = student_list.filter(student__ID__iexact=id)
        return render(self.request, 'students/search_student_result.html',
                      context={'active_student_list': student_list})


class DeleteStudentView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('student:student_list')

    def get_object(self, queryset=None):
        return Student.objects.get(pk=self.request.GET.get('pk'))


class ModifyStudentView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'students.modifyStudent'
    model = Student
    template_name = 'students/modify_student_form.html'
    success_url = reverse_lazy("student:student_list")

    def get_object(self):
        return Student.objects.get(pk=self.request.GET.get('id'))


class ModifyStudentLookUpView(PermissionRequiredMixin, generic.FormView):
    permission_required = 'students.changeInfo'
    form_class = ModifyStudentForm
    template_name = 'students/modify_student_lookup_form.html'
    result_template_name = 'students/modify_student_lookup_form_result.html'
    table_class = StudentTable

    def get_table_kwargs(self):
        return {
            'empty_text': 'No results matching query.'
        }

    def filter_table_data(self, form):
        return Student.objects.filter(client__pk__exact=form.cleaned_data['id'])

from typing import Any, Union

from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from students.forms import StudentForm, SearchStudentForm, ModifyStudentInfoForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from students.tables import StudentTable
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .models import Student
from django.core.exceptions import ImproperlyConfigured



class index(generic.TemplateView):
    template_name = 'students/index.html'


class StudentListView(PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'students/student_list.html'
    permission_required = 'students.viewStudents'
    table_class = StudentTable

    def get_table_kwargs(self):
        user = self.request.user
        if user.has_perms('student.modifyStudent') or user.has_perms('student.delete_student'):
            return {'empty_text': 'No Student in the database.'}
        return {'exclude': ('select', 'actions'), 'empty_text': 'No Student in the database.'}


class AddStudentView(PermissionRequiredMixin, generic.CreateView):
    model = Student
    context_object_name = 'add_student'
    template_name = 'students/add_new_student.html'
    permission_required = 'students.addStudents'
    form_class = StudentForm
    success_url = reverse_lazy('students:student_list')


class StudentHomeView(PermissionRequiredMixin, generic.ListView):
    model = Student
    context_object_name = 'student_home'
    template_name = 'students/StudentHomeView.html'
    permission_required = 'students.home'


class FormTableView(SingleTableMixin, generic.FormView):
    result_template_name = None
    table_data = {}

    def filter_table_data(self, form):
        return None

    def form_valid(self, form):
        self.table_data = self.filter_table_data(form)
        return render(self.request, self.result_template_name, context=self.get_context_data(form=form))


class SearchStudentView(PermissionRequiredMixin, FormTableView):
    permission_required = 'students.searchStudents'
    template_name = 'students/search_student.html'
    result_template_name = 'students/search_student_result.html'
    form_class = SearchStudentForm
    table_class = StudentTable

    def get_table_kwargs(self):
        return {
            'empty_text': 'No results matching query.'
        }

    def filter_table_data(self, form):
        print(Student.objects.none())
        student_list = Student.objects
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        cellPhone = form.cleaned_data['cellPhone']
        email = form.cleaned_data['email']
        ssn = form.cleaned_data['ssn']
        zipcode = form.cleaned_data['zipcode']

        if not any((first_name, last_name, cellPhone, ssn, zipcode)):
            return Student.objects.none()

        if first_name:
            student_list = student_list.filter(first_name__iexact=first_name)
        if last_name:
            student_list = student_list.filter(last_name__iexact=last_name)
        if cellPhone:
            student_list = student_list.filter(cellPhone__exact=cellPhone)
        if email:
            student_list = student_list.filter(email__iexact=email)
        if ssn:
            student_list = student_list.filter(email__exact=ssn)
        if zipcode:
            student_list = student_list.filter(email__exact=zipcode)
        return student_list


class DeleteStudentView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'students.deleteStudent'
    model = Student
    context_object_name = 'delete_student'
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:student_list')

    def get_object(self, queryset=None):
        return Student.objects.get(pk=self.request.GET.get('student_id'))


class ModifyStudentView(PermissionRequiredMixin, generic.UpdateView):
    model = Student
    permission_required = 'students.modifyStudent'
    context_object_name = 'modify_student'
    template_name = 'students/modify_student_form.html'
    form_class = ModifyStudentInfoForm
    success_url = reverse_lazy("students:student_list")

    def get_object(self):
        return Student.objects.get(pk=self.request.GET.get('student_id'))





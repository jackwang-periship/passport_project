from typing import Any, Union

from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from students.forms import StudentForm, SearchStudentForm, ModifyStudentForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from students.tables import StudentTable, StudentSearchTable
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .models import Student
from students.filter import StudentFilter


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
            return {'empty_text': 'No Student in the list.'}
        return {'exclude': ('select', 'actions'), 'empty_text': 'No Student in the list.'}


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

    def filter_table_data(self, form):
        return None

    def get_context_data(self, **kwargs):
        context = super(generic.FormView, self).get_context_data(**kwargs)
        if 'form' not in context or not context['form'].is_valid():
            return context
        table = self.get_table(**self.get_table_kwargs())
        context[self.get_context_table_name(table)] = table
        return context

    def form_valid(self, form):
        self.filter_table_data(form)
        return render(self.request, self.result_template_name, context=self.get_context_data(form=form))


class SearchStudentView(SingleTableMixin, FilterView):
    model = Student
    template_name = 'students/search_student.html'
    result_template_name = 'students/search_student_result.html'
    table_class = StudentSearchTable
    form_class = SearchStudentForm
    # filterset_class = StudentFilter
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

        if not any((first_name, last_name, cellPhone)):
            return Student.objects.none()

        if first_name:
            student_list = student_list.filter(first_name__iexact=first_name)
        if last_name:
            student_list = student_list.filter(last_name__iexact=last_name)
        if cellPhone:
            student_list = student_list.filter(cellPhone__iexact=cellPhone)
        return student_list


class DeleteStudentView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def get_object(self, queryset=None):
        return Student.objects.get(pk=self.request.GET.get('pk'))


class MultipleDeleteView(generic.View):
    http_method_names = ['post']
    model = None
    success_url = None

    def get_next_page(self, request):
        print(request.POST.get('next-view-name'))
        if request.POST.get('next-view-name'):
            return reverse(request.POST.get('next-view-name'))
        return self.success_url

    def post(self, request, *args, **kwargs):
        row_pks = request.POST.getlist('row_pks')
        rows = self.model.objects.filter(pk__in=row_pks)
        rows.delete()
        return redirect(self.get_next_page(request))


class DeleteStudentView(MultipleDeleteView):
    http_method_names = ['post']
    success_url = reverse_lazy('students:index')
    model = Student


class ModifyStudentView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'students.modifyStudent'
    model = Student
    template_name = 'students/modify_student_form.html'
    fields = ['cellphone', 'email', 'address', 'city', 'country']
    success_url = reverse_lazy("students:student_list")

    def get_object(self):
        return Student.objects.get(pk=self.request.GET.get('id'))


class ModifyStudentLookUpView(PermissionRequiredMixin, generic.FormView):
    permission_required = 'students.modifyStudent'
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

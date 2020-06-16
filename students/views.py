from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin

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
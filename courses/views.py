from django.views import generic
from django.views.generic.edit import CreateView
from .models import Course
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormView
from .forms import CourseForm
from django.shortcuts import reverse


class CourseListView(PermissionRequiredMixin, generic.ListView):
    model = Course
    context_object_name = 'course_list'  # your own name for the list as a template variable
    queryset = Course.objects.filter  # Get all the employees
    template_name = 'courses/course_list.html' # Specify your own template name/location
    permission_required = 'courses.can_list_courses'

    def get_queryset(self):
        return Course.objects.all()  # Get all employees

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(CourseListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context["sidebar_data"] = 'This holds the sidebar data for courses'
        return context


class CourseDetailView(generic.DetailView):
    model = Course


class NewCourseView(PermissionRequiredMixin, FormView):
    model = Course
    context_object_name = 'course_new'  # your own name for the list as a template variable
    template_name = 'courses/course_new.html'  # Specify your own template name/location
    form_class = CourseForm
    permission_required = 'add_course'

    def form_valid(self, form):
        form.save(self.request.user)
        return super(NewCourseView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("courses:list_courses")


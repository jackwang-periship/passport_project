from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from .models import Attendances

# Create your views here.
from django.views import generic


class AttedancesListView( generic.ListView):

    #In overview
    # Call def queryset
    #The quesryset return the result you specify for .all()
    #The return value is save in context_object_name
    #The contect_object_name stores the resutl in attedance_list_for_roday
    model = Attendances
    #Has to match in your showStudentAttendance.html in the template, attendance directory.
    context_object_name = 'attendance_list_for_today'  # your own name for the list as a template variable
    queryset = Attendances.objects.filter  # Get all the students attendance
    template_name = 'attendances/showStudentAttendance.html' # Specify your own template name/location


    def get_queryset(self):
        #You choice  the the number of records to return. In this example .all() method was use to return all object.
        #Anothe example .order_by('-pub_date')[:5]
        #Anthoer example return Course.objects.order_by('name')[:10]

        # Depends on model. Read the book tangoWithDjango
        # return Attendances.objects.all()
        return Attendances.objects.order_by('last_name')[:10]
        # Get all employees

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AttedancesListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context["sidebar_data"] = 'This holds the sidebar data for courses'
        return context


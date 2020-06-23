from django.shortcuts import render
from .models import Schedule
import django_tables2 as tables
from django.views.generic import UpdateView
from django.views.generic import ListView

#NOTE:  pendingList and scheduleList are the only views I have worked on,
#       the rest of these only lead to blank templates that extend the base.
def index(request):
    return render(request, 'schedule/index.html')


class ScheduleList(ListView):
    def get_context_data(self, **kwargs):
        context = {
            'listType' : 'schedule',
            'list' : Schedule.objects.filter(approved=True),
            'actions':  {'update', 'delete'}
        }
        return context

    queryset = Schedule.objects.filter(approved=True),
    template_name =  'schedules/lists.html'


class PendingList(ListView):
    def get_context_data(self, **kwargs):
        context = {
            'listType' : 'Pending',
            'actions' : {'approve', 'update', 'delete'}

        }
        return context

    queryset = Schedule.objects.filter(approved=False),
    template_name =  'schedules/lists.html'


class UpdateSchedules(UpdateView):
    model = Schedule
    fields = [
        "course_name",
        "location",
        "start_date",
        "end_date",
        "time",
        "hours",
        "instructor"
    ]
    sucsess_url ='/'

def daily(request):
    return render(request, 'schedules/daily.html')


def weekly(request):
    return render(request, 'schedules/weekly.html')


def officeSchedule(request):
    return render(request, 'schedules/officeSchedule.html')


def yearlySchedule(request):
    return render(request, 'schedules/yearlySchedule.html')


def startOne(request):
    return render(request, 'schedules/startOne.html')


def help(request):
    return render(request, 'schedules/help.html')

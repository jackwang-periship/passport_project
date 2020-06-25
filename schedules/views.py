from django.shortcuts import render
from .models import Schedule
from django_tables2.views import SingleTableView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .tables import ScheduleTable

#NOTE:  pendingList and scheduleList are the only views I have worked on,
#       the rest of these only lead to blank templates that extend the base.
def index(request):
    return render(request, 'schedule/index.html')


class ScheduleList(PermissionRequiredMixin, SingleTableView):
    def get_context_data(self, **kwargs):
        list = Schedule.objects.filter(approved=True)
        context = {
            'listType' : 'schedule',
            'list' : list,
            'actions':  {'update', 'delete'},
            'length' : len(list)
        }
        return context

    table_class = ScheduleTable
    template_name =  'schedules/lists.html'
    permission_required = "schedule.can_view_schedule"
    queryset = Schedule.objects.filter(approved=True)


class PendingList(PermissionRequiredMixin, SingleTableView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        list = Schedule.objects.filter(approved=False)
        context.update({
            'listType' : 'Pending',
            'list' : list,
            'length' : len(list)
        })
        return context
    table_class = ScheduleTable
    table_data = queryset = Schedule.objects.filter(approved=False)
    template_name =  'schedules/lists.html'
    permission_required = "schedule.can_view_pending_schedule"



class UpdateSchedules(PermissionRequiredMixin, UpdateView):
    fields = [
        "course_name",
        "location",
        "start_date",
        "end_date",
        "time",
        "hours",
        "instructor"
    ]
    model = Schedule
    template_name = "schedules/schedule_update.html"
    success_url = '/schedules/schedulelist'
    permission_required = "schedule.can_update_schedule"

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

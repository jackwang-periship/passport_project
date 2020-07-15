from django.shortcuts import render
from .models import Schedule

#NOTE:  pendingList and scheduleList are the only views I have worked on,
#       the rest of these only lead to blank templates that extend the base.
def index(request):
    return render(request, 'schedule/index.html')


def scheduleList(request):
    mylist = Schedule.objects.filter(approved=True)
    actions = {'update', 'delete'}
    context = {
        'listType' : 'schedule',
        'list': mylist,
        'actions': actions

    }
    return render(request, 'schedules/lists.html', context)


def pendingList(request):
    mylist = Schedule.objects.filter(approved=False)
    actions = {'approve', 'update', 'delete'}
    context = {
        'listType' : 'Pending',
        'list' : mylist,
        'actions' : actions

    }
    return render(request, 'schedules/lists.html', context)


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

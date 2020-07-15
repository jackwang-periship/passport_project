# URL Patterns for the schedule section
from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.index, name='index'),
    path('schedulelist', views.scheduleList, name='schedulelist'),
    path('pendinglist', views.pendingList, name='pendinglist'),
    path('dailyto-do', views.daily, name='dailyto-do'),
    path('weeklyto-do', views.weekly, name='weeklyto-do'),
    path('officeschedule', views.officeSchedule, name='officeschedule'),
    path('yearlyschedule', views.yearlySchedule, name = 'yearlyschedule'),
    path('startone', views.startOne, name = 'startone'),
    path('help', views.help, name = 'help'),

]

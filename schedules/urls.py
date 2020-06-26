# URL Patterns for the schedule section
from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.index, name='index'),
    path('schedulelist', views.ScheduleList.as_view(), name='schedulelist'),
    path('pendinglist', views.PendingList.as_view(), name='pendinglist'),
    path('<pk>/update', views.UpdateSchedules.as_view(), name='update'),
    path('<pk>/approve', views.ApproveSchedules.as_view(), name='approve'),
    path('<pk>/delete', views.DeleteSchedule.as_view(), name='delete'),
    path('dailyto-do', views.daily, name='dailyto-do'),
    path('weeklyto-do', views.weekly, name='weeklyto-do'),
    path('officeschedule', views.officeSchedule, name='officeschedule'),
    path('yearlyschedule', views.yearlySchedule, name = 'yearlyschedule'),
    path('startone', views.startOne, name = 'startone'),
    path('help', views.help, name = 'help'),

]

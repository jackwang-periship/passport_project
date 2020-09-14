#List all urls.
#urls case sentive lower case

# Use include() to add paths from the home application
from django.urls import path
from . import views

app_name = 'attendances'

urlpatterns = [
    path('list/', views.AttedancesListView.as_view(), name='list_students_attendances'),
    #Created this form following this tutorial https://tutorial.djangogirls.org/en/django_forms/
    path('add/', views.post_new, name='post_new_attendance_record')



]

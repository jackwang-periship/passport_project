#List all urls.
#urls case sentive lower case

# Use include() to add paths from the home application
from django.urls import path
from . import views

app_name = 'attendances'

urlpatterns = [                                     #For templates reference
    path('list/', views.AttedancesListView.as_view(), name='list_students_attendances'),

]

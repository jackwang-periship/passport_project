from django.urls import path
from administration.views import ChangePasswordView, AddUserView

app_name = 'administration'

urlpatterns = [
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('add_user/', AddUserView.as_view(), name='add_user'),
]

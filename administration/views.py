from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from administration.forms import ChangePasswordForm, AddUserForm


class ChangePasswordView(FormView):
    form_class = ChangePasswordForm
    template_name = 'administration/change_password_form.html'
    success_url = reverse_lazy('administration:change_password')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['new_password']

        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        return super().form_valid(form)

class AddUserView(FormView):
    form_class = AddUserForm
    template_name = 'administration/add_user_form.html'
    success_url = reverse_lazy('administration:add_user')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        groups = form.cleaned_data['groups']

        user = User.objects.create_user(username=username, email=email, password=password)

        for group in groups:
            user.groups.add(group)

        return super().form_valid(form)

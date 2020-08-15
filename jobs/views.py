from django.shortcuts import render
from django_tables2.views import SingleTableView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
import datetime
from .models import Posting, Client
from .tables import ClientTable, PostingTable, EditTable
from .forms import PostingForm

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

class UpdatePostings(UpdateView, PermissionRequiredMixin):
    fields = [
        'title',
        'location',
        'deadline',
        'position',
    ]
    model = Posting
    template_name = 'jobs/updatePostings.html'
    permission_required = 'jobs.can_update_posting'
    success_url = '/jobs/editpostings'

class ClientListings(SingleTableView, PermissionRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    table_class = ClientTable
    template_name = 'jobs/clientListings.html'
    table_data = queryset = Client.objects.all()
    permission_required = 'jobs.company_user'

class UpdateProfile(UpdateView, PermissionRequiredMixin):
    fields = [
        'contactName',
        'contactEmail',
        'companyAddress',
    ]
    model = Client
    template_name = 'jobs/updateProfile.html'
    success_url = '/jobs'
    permission_required = 'jobs.can_update_client'

class CreatePosting(CreateView, PermissionRequiredMixin):
    model = Posting
    form_class = PostingForm
    permission_required = 'jobs.can_create_posting'
    template_name = 'jobs/createPosting.html'
    success_url = '/jobs'
    def form_valid(self, form):
        model = form.save(commit=False)
        form.instance.client = self.request.user.companyuser.client
        print(form)
        return super(CreatePosting, self).form_valid(form)



class ClientPostings(SingleTableView, PermissionRequiredMixin):
    table_class = PostingTable
    template_name = 'jobs/clientListings.html'
    permission_required = 'jobs.can_apply'
    def get_table_data(self):
        return Posting.objects.filter(client=Client(self.kwargs['clientId']))
    def get_queryset(self):
        return Posting.objects.filter(client=Client(self.kwargs['clientId']))

class ModeratePostings(SingleTableView, PermissionRequiredMixin):
    table_class = EditTable
    template_name = 'jobs/clientListings.html'
    permission_required = 'jobs.can_update_posting'
    def get_table_data(self):
        return Posting.objects.filter(client=self.request.user.companyuser.client)
    def get_queryset(self):
        return Posting.objects.filter(client=self.request.user.companyuser.client)

class DeletePosting(DeleteView, PermissionRequiredMixin):
    model = Posting
    template_name = 'jobs/deletePosting.html'
    permission_required = 'jobs.can_delete_posting'
    success_url = '/jobs/editpostings'

class Apply(CreateView, PermissionRequiredMixin):
    model = Posting
    template_name = 'jobs/Apply.html'
    permission_required = 'jobs.can_apply'
    form_class = PostingForm
    success_url = 'jobs/createposting'
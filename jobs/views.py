from django.shortcuts import render
from django_tables2.views import SingleTableView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
import datetime
from .models import Posting, Client
from .tables import ClientTable, PostingTable
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
    success_url = '/jobs/1/postings'

class ClientListings(SingleTableView, PermissionRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    table_class = ClientTable
    template_name = 'jobs/clientListings.html'
    table_data = queryset = Client.objects.all()

class UpdateProfile(UpdateView, PermissionRequiredMixin):
    fields = [
        'contactName',
        'contactEmail',
        'companyAddress',
    ]
    model = Client
    template_name = 'jobs/updateProfile.html'
    success_url = '/jobs'

class CreatePosting(CreateView, PermissionRequiredMixin):
    model = Posting
    form_class = PostingForm
    def form_valid(self, form):
        model = form.save(commit=False)
        form.instance.client = Client(1)
        print(form)
        return super(CreatePosting, self).form_valid(form)
    template_name = 'jobs/createPosting.html'
    success_url = '/jobs'


class ClientPostings(SingleTableView, PermissionRequiredMixin):
    clientId = 0
    table_class = PostingTable
    template_name = 'jobs/clientListings.html'
    print()
    table_data = queryset = Posting.objects.filter(client=Client(1))

class DeletePosting(DeleteView, PermissionRequiredMixin):
    model = Posting
    template_name = 'jobs/deletePosting.html'
    success_url = '/jobs/1/postings'
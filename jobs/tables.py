from django_tables2 import tables
from django_tables2 import columns
from .models import Client, Posting

class ClientTable(tables.Table):
    postings = columns.TemplateColumn(template_name="jobs/client_buttons.html", orderable=False)
    class Meta:
        model = Client
        template_name = 'django_tables2/bootstrap.html'
        fields = ('company', 'contactName', 'contactEmail', 'companyAddress')

class EditTable(tables.Table):
    postings = columns.TemplateColumn(template_name="jobs/edit_buttons.html", orderable=False)
    class Meta:
        model = Posting
        template_name = 'django_tables2/bootstrap.html'
        fields = ('title', 'location', 'deadline', 'postedDate', 'position')

class PostingTable(tables.Table):
    postings = columns.TemplateColumn(
        template_code="<a href='/jobs/{{ record.pk }}/apply' class='btn btn-light'>Apply</a>", orderable=False)
    class Meta:
        model = Posting
        template_name = 'django_tables2/bootstrap.html'
        fields = ('title', 'location', 'deadline', 'postedDate', 'position')
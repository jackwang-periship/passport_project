from django.shortcuts import render, redirect
from wiawdp.forms import FindStudentForm, ViewReportForm, ModifyContractLookupForm
from django.urls import reverse_lazy, reverse
from wiawdp.models import Contract, WIAWDP
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, DeleteView, View
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin
from wiawdp.tables import ContractTable, WIAWDPTable
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView
import django_filters


class IndexView(TemplateView):
    template_name = 'wiawdp/index.html'


class ContractFilter(django_filters.FilterSet):
    CONTRACT_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )
    end_date = django_filters.ChoiceFilter(label='Contract Status', choices=CONTRACT_CHOICES, method='filter_active')

    class Meta:
        model = Contract
        fields = ['end_date']

    def filter_active(self, queryset, name, value):
        if value == 'active':
            return queryset.filter(end_date__gte=datetime.today())
        if value == 'inactive':
            return queryset.filter(end_date__lt=datetime.today())
        return queryset


class ContractView(PermissionRequiredMixin, SingleTableMixin, FilterView):
    permission_required = 'wiawdp.view_contract'
    template_name = 'wiawdp/contracts.html'
    model = Contract
    # table_data = Contract.objects.filter(end_date__gte=datetime.today())
    table_class = ContractTable
    filterset_class = ContractFilter

    def get_table_kwargs(self):
        user = self.request.user
        if user.has_perms('wiawdp.change_contract') or user.has_perms('wiawdp.delete_contract'):
            return {'empty_text': 'No active contracts.'}
        return {'exclude': ('select', 'actions'), 'empty_text': 'No active contracts.'}


class AddContractView(PermissionRequiredMixin, CreateView):
    permission_required = 'wiawdp.add_contract'
    model = Contract
    template_name = 'wiawdp/add_contract_form.html'
    success_url = reverse_lazy('wiawdp:active_contracts')
    fields = ['client', 'workforce', 'end_date', 'performance']



class FormTableView(SingleTableMixin, FormView):
    result_template_name = None

    def filter_table_data(self, form):
        return None

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        if 'form' not in context or not context['form'].is_valid():
            return context
        table = self.get_table(**self.get_table_kwargs())
        context[self.get_context_table_name(table)] = table
        return context

    def form_valid(self, form):
        self.table_data = self.filter_table_data(form)
        return render(self.request, self.result_template_name, context=self.get_context_data(form=form))


class SearchContractsView(PermissionRequiredMixin, FormTableView):
    permission_required = ('wiawdp.view_contract', 'wiawdp.view_person')
    template_name = 'wiawdp/search_contracts_form.html'
    result_template_name = 'wiawdp/search_contracts_results.html'
    form_class = FindStudentForm
    table_class = ContractTable

    def get_table_kwargs(self):
        return {
            'empty_text': 'No results matching query.'
        }

    def filter_table_data(self, form):
        print(Contract.objects.none())
        contract_list = Contract.objects
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        ssn = form.cleaned_data['ssn']
        email = form.cleaned_data['email']
        home_phone = form.cleaned_data['home_phone']
        cell_phone = form.cleaned_data['cell_phone']
        zipcode = form.cleaned_data['zipcode']

        if not any((first_name, last_name, ssn, email, home_phone, cell_phone, zipcode)):
            return Contract.objects.none()

        if first_name:
            contract_list = contract_list.filter(client__first_name__iexact=first_name)
        if last_name:
            contract_list = contract_list.filter(client__last_name__iexact=last_name)
        if ssn:
            contract_list = contract_list.filter(client__ssn__iexact=ssn)
        if email:
            contract_list = contract_list.filter(client__email__iexact=email)
        if home_phone:
            contract_list = contract_list.filter(client__homePhone=home_phone)
        if cell_phone:
            contract_list = contract_list.filter(client__cellPhone__iexact=cell_phone)
        if zipcode:
            contract_list = contract_list.filter(client__zipcode__iexact=zipcode)

        return contract_list


class ModifyContractView(PermissionRequiredMixin, UpdateView):
    permission_required = 'wiawdp.change_contract'
    model = Contract
    template_name = 'wiawdp/modify_contract_form.html'
    fields = ['workforce', 'end_date', 'performance']
    success_url = reverse_lazy('wiawdp:active_contracts')

    def get_object(self):
        return Contract.objects.get(pk=self.request.GET.get('contract_id'))


class ModifyContractLookupView(PermissionRequiredMixin, FormTableView):
    permission_required = 'wiawdp.change_contract'
    template_name = 'wiawdp/modify_contract_lookup_form.html'
    result_template_name = 'wiawdp/modify_contract_lookup_results.html'
    form_class = ModifyContractLookupForm
    table_class = ContractTable

    def get_table_kwargs(self):
        return {
            'empty_text': 'No results matching query.'
        }

    def filter_table_data(self, form):
        return Contract.objects.filter(client__pk__exact=form.cleaned_data['student_id'])

class ReportView(PermissionRequiredMixin, FormTableView):
    permission_required = 'wiawdp.view_wiawdp'
    template_name = 'wiawdp/view_report.html'
    result_template_name = 'wiawdp/report.html'
    form_class = ViewReportForm
    success_url = reverse_lazy('wiawdp:index')
    model = WIAWDP
    table_class = WIAWDPTable

    def get_table_kwargs(self):
        return {
            'empty_text': 'No results matching query.'
        }

    def filter_table_data(self, form):
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        eatontown = form.cleaned_data[WIAWDP.EATONTOWN.lower()]
        fairfield = form.cleaned_data[WIAWDP.FAIRFIELD.lower()]
        south_plainfield = form.cleaned_data[WIAWDP.SOUTH_PLAINFIELD.lower()]

        locations = []
        if eatontown:
            locations.append(WIAWDP.EATONTOWN)
        if fairfield:
            locations.append(WIAWDP.FAIRFIELD)
        if south_plainfield:
            locations.append(WIAWDP.SOUTH_PLAINFIELD)

        return WIAWDP.objects.filter(date_approved__range=(start_date, end_date)).filter(location__in=locations)


class WIAWDPView(SingleTableView):
    model = WIAWDP
    table_data = WIAWDP.objects.all()
    table_class = WIAWDPTable
    template_name = 'wiawdp/programs.html'


class DeleteContractView(DeleteView):
    model = Contract
    success_url = reverse_lazy('wiawdp:active_contracts')

    def get_object(self, queryset=None):
        return Contract.objects.get(pk=self.request.POST.get('pk'))

class MultipleDeleteView(View):
    http_method_names = ['post']
    model = None
    success_url = None

    def get_next_page(self, request):
        print(request.POST.get('next-view-name'))
        if request.POST.get('next-view-name'):
            return reverse(request.POST.get('next-view-name'))
        return self.success_url

    def post(self, request, *args, **kwargs):
        row_pks = request.POST.getlist('row_pks')
        rows = self.model.objects.filter(pk__in=row_pks)
        rows.delete()
        return redirect(self.get_next_page(request))

class DeleteContractsView(MultipleDeleteView):
    http_method_names = ['post']
    success_url = reverse_lazy('wiawdp:index')
    model = Contract

from django.shortcuts import render
from wiawdp.forms import FindStudentForm, ViewReportForm, ModifyContractLookupForm
from django.urls import reverse_lazy
from wiawdp.models import Contract, CareerPathway
from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin


class IndexView(TemplateView):
    template_name = 'wiawdp/index.html'


class SearchView(PermissionRequiredMixin, FormView):
    permission_required = 'wiawdp.view_contract'
    template_name = 'wiawdp/index.html'
    form_class = FindStudentForm


class ActiveContractView(PermissionRequiredMixin, TemplateView):
    permission_required = 'wiawdp.view_contract'
    template_name = 'wiawdp/active_contracts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_contract_list'] = Contract.objects.filter(end_date__gte=datetime.today())
        return context


class AddContractView(PermissionRequiredMixin, CreateView):
    permission_required = 'wiawdp.add_contract'
    model = Contract
    template_name = 'wiawdp/add_contract.html'
    success_url = reverse_lazy('wiawdp:active_contracts')
    fields = ['client', 'workforce', 'end_date', 'performance']


class ReportView(PermissionRequiredMixin, FormView):
    permission_required = 'wiawdp.view_contract'
    template_name = 'wiawdp/view_report.html'
    form_class = ViewReportForm
    success_url = reverse_lazy('wiawdp:index')

    def form_valid(self, form):
        return render(self.request, 'wiawdp/report.html', )


class SearchContractView(PermissionRequiredMixin, FormView):
    permission_required = ('wiawdp.view_contract', 'wiawdp.view_person')
    template_name = 'wiawdp/search_contracts.html'
    form_class = FindStudentForm

    def form_valid(self, form):
        contract_list = Contract.objects
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        ssn = form.cleaned_data['ssn']
        email = form.cleaned_data['email']
        home_phone = form.cleaned_data['home_phone']
        cell_phone = form.cleaned_data['cell_phone']
        zipcode = form.cleaned_data['zipcode']

        if not any((first_name, last_name, ssn, email, home_phone, cell_phone, zipcode)):
            return render(self.request, 'wiawdp/search_contracts_result.html',
                          context={'active_contract_list': []})

        if first_name:
            contract_list = contract_list.filter(client__first_name__iexact=first_name)
        if last_name:
            contract_list = contract_list.filter(client__last_name__iexact=last_name)
        if ssn:
            contract_list = contract_list.filter(client__ssn__iexact=ssn)
        if email:
            contract_list = contract_list.filter(client__email__iexact=email)
        if home_phone:
            contract_list = contract_list.filter(client__home_phone__iexact=home_phone)
        if cell_phone:
            contract_list = contract_list.filter(client__cell__phone__iexact=cell_phone)
        if zipcode:
            contract_list = contract_list.filter(client__address__zipcode__iexact=zipcode)
        return render(self.request, 'wiawdp/search_contracts_result.html',
                      context={'active_contract_list': contract_list})


class ModifyContract(PermissionRequiredMixin, UpdateView):
    permission_required = 'wiawdp.change_contract'
    model = Contract
    template_name = 'wiawdp/modify_contract.html'
    fields = ['client', 'workforce', 'end_date', 'performance']
    success_url = reverse_lazy('wiawdp:active_contracts')

    def get_object(self):
        return Contract.objects.get(pk=self.request.GET.get('contract_id'))


class ModifyContractLookup(PermissionRequiredMixin, FormView):
    permission_required = 'wiawdp.change_contract'
    template_name = 'wiawdp/modify_contract_lookup.html'
    form_class = ModifyContractLookupForm

    def form_valid(self, form):
        contract_list = Contract.objects.filter(client__uuid__exact=form.cleaned_data['student_id'])
        return render(self.request, 'wiawdp/modify_contract_lookup_results.html',
                      context={'contract_list': contract_list})


class CareerPathwayView(TemplateView):
    template_name = 'wiawdp/career_pathways.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pathways'] = CareerPathway.objects.all()
        return context
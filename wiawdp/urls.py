from django.urls import path
from wiawdp.views import IndexView, AddContractView, ReportView, ModifyContractView, ModifyContractLookupView, \
    ContractView, SearchContractsView, WIAWDPView, DeleteContractView, DeleteContractsView

app_name = 'wiawdp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contracts/', ContractView.as_view(), name='active_contracts'),
    path('add_contract/', AddContractView.as_view(), name='add_contract'),
    path('view_report/', ReportView.as_view(), name='view_report'),
    path('search_contracts/', SearchContractsView.as_view(), name='search_contracts'),
    path('modify_contract_lookup/', ModifyContractLookupView.as_view(), name='modify_contract_lookup'),
    path('modify_contract/', ModifyContractView.as_view(), name='modify_contract'),
    path('programs/', WIAWDPView.as_view(), name='available_programs'),
    path('delete_contract/', DeleteContractView.as_view(), name='delete_contract'),
    path('delete_contracts/', DeleteContractsView.as_view(), name='delete_contracts'),
    path('wiawdp/', WIAWDPView.as_view(), name="wiawdp")
]

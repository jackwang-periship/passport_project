from django.urls import path
from . import views
from wiawdp.views import IndexView, AddContractView, ReportView, ModifyContract, ModifyContractLookup, ActiveContractView, SearchContractView, CareerPathwayView

app_name = 'wiawdp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('active_contracts/', ActiveContractView.as_view(), name='active_contracts'),
    path('add_contract/', AddContractView.as_view(), name='add_contract'),
    path('view_report/', ReportView.as_view(), name='view_report'),
    path('search_contracts/', SearchContractView.as_view(), name='search_contracts'),
    path('modify_contract_lookup/', ModifyContractLookup.as_view(), name='modify_contract_lookup'),
    path('modify_contract/', ModifyContract.as_view(), name='modify_contract'),
    path('career_pathways/', CareerPathwayView.as_view(), name='available_programs'),
]
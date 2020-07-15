from django.contrib import admin
from wiawdp.models import Workforce, Contract

admin.site.register(Workforce)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'workforce', 'end_date', 'performance')


admin.site.register(Contract, ContractAdmin)

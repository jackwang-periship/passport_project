from django.contrib import admin
from wiawdp.models import Workforce, Contract, WIAWDP

admin.site.register(Workforce)
admin.site.register(WIAWDP)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'workforce', 'end_date', 'performance')


admin.site.register(Contract, ContractAdmin)

from django.contrib import admin
from wiawdp.models import Workforce, Contract, Person, Address
# Register your models here.
admin.site.register(Workforce)
# admin.site.register(Location)
# admin.site.register(Contract)

class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'workforce', 'end_date', 'performance')

admin.site.register(Contract, ContractAdmin)
admin.site.register(Person)
admin.site.register(Address)
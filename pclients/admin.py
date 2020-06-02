from django.contrib import admin
from .models import Pclient, Paddress

@admin.register(Pclient)
class PclientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'company_name', 'title', 'phone')

@admin.register(Paddress)
class Paddress(admin.ModelAdmin):
    list_display = ('address', 'city', 'state', 'zipcode')

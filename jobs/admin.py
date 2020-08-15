from django.contrib import admin
from .models import Client, Posting, Applicant, CompanyUser
# Register your models here.
@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display =('pk', 'company', 'contactName', 'contactEmail', 'companyAddress')
@admin.register(Posting)
class Posting(admin.ModelAdmin):
    list_display = ('pk', 'title', 'location', 'deadline', 'postedDate', 'position', 'client')
@admin.register(Applicant)
class Applicant(admin.ModelAdmin):
    list_display = ('user', 'posting')
@admin.register(CompanyUser)
class CompanyUser(admin.ModelAdmin):
    list_display = ('user', 'client')
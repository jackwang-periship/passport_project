from django.contrib import admin

# Register your models here.
class TransAdmin(admin.ModelAdmin):
    list_display = ('verifiedId', 'course', 'date')
    # prepopulated_fields = {'slug':('name',)}

class VerifAdmin(admin.ModelAdmin):
    list_display = ('studentId',)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('type', 'startD', 'endD')

from .models import Transaction, VerifiedId, Report
admin.site.register(Transaction, TransAdmin)
admin.site.register(VerifiedId, VerifAdmin)
admin.site.register(Report, ReportAdmin)


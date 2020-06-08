from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Employee

# Register your models here.
admin.site.register(UserProfile)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'department', 'role')

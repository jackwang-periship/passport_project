from django.contrib import admin
from .models import Schedule

# Register your models here.
@admin.register(Schedule)
class Schedule(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'location', 'start_date', 'end_date', 'time', 'hours', 'instructor')

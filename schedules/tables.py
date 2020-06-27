from django_tables2 import tables
from django_tables2 import columns
from .models import Schedule

class ScheduleTable(tables.Table):
    course_name = columns.Column(verbose_name="Course")
    actions = columns.TemplateColumn(template_name="schedules/buttons.html", orderable=False)
    class Meta:
        model = Schedule
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'course_name', 'location', 'start_date', 'end_date', 'time', 'hours', 'instructor', 'actions')

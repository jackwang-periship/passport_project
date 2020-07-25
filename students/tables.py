from students.models import Student
import django_tables2 as tables

class StudentTable(tables.Table):
    pk = tables.Column(verbose_name='RecId')
    actions = tables.TemplateColumn(template_name="students/buttons.html", orderable=False)

    class Meta:
        model = Student
        template_name = 'django_tables2/bootstrap.html'
        fields = ('pk', 'first_name', 'last_name', 'address', 'cellPhone', 'email', 'created_on', 'actions')

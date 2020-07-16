from students.models import Student
import django_tables2 as tables

class StudentTable(tables.Table):
    pk = tables.Column(verbose_name='RecId')
    full_name = tables.Column(accessor='Student.full_name', order_by=('Student__first_name', 'Student__last_name'))

    class Meta:
        model = Student
        template_name = 'django_tables2/bootstrap.html'
        fields = (
            'first_name', 'last_name', 'ssn', 'zipcode', 'country', 'city', 'cellPhone', 'email',
            'location',
            'refer', 'sources', 'gender')
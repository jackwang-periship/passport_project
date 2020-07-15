import django_tables2 as tables
from .models import Transaction, Report


class Notice(tables.Table):
    class Meta:
        model = Transaction
        template_name = "django_tables2/bootstrap.html"
        fields = ("verifiedId", "firstName", "lastName", "counselor", "course", "balance", "date" )


class Logs(tables.Table):
    class Meta:
        model = Report
        template_name = "django_tables2/bootstrap.html"
        fields = ("verifiedId", "firstName", "lastName", "counselor", "course", "balance", "date" )


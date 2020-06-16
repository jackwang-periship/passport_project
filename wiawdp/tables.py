from wiawdp.models import Contract
import django_tables2 as tables


class ContractTable(tables.Table):
    pk = tables.Column(verbose_name='RecId')
    full_name = tables.Column(accessor='client.full_name', order_by=('client__first_name', 'client__last_name'))

    class Meta:
        model = Contract
        template_name = 'django_tables2/bootstrap.html'
        fields = ('pk', 'full_name', 'workforce', 'end_date', 'performance')


class ContractTableEditable(tables.Table):
    pk = tables.Column(verbose_name='RecId')
    client = tables.Column()
    actions = tables.TemplateColumn("""
<form method="get" action="{% url 'wiawdp:modify_contract' %}">
    <input type="hidden" name="contract_id" value="{{ record.id }}">
    <input type="submit" value="Edit" class="btn btn-info">
</form>
<form method="get" action="{% url 'wiawdp:delete_contract' %}">
    <input type="hidden" name="pk" value="{{ record.pk }}">
    <input type="submit" value="Delete" class="btn btn-danger">
</form>
    """, orderable=False)

    def render_client(self, value, record):
        return f'{value.first_name} {value.last_name} ({value.pk})'

    class Meta:
        model = Contract
        template_name = 'django_tables2/bootstrap.html'
        fields = ('pk', 'client', 'workforce', 'end_date', 'performance')

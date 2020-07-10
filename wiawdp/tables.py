from wiawdp.models import Contract, WIAWDP
import django_tables2 as tables


class ContractTable(tables.Table):
    row_pks = tables.CheckBoxColumn({'th__input': {'id': 'checkbox-all-toggle'}, 'td__input': {'form': 'delete-form'}},
                                    accessor='pk')
    pk = tables.Column(verbose_name='RecId')
    client = tables.Column()
    actions = tables.TemplateColumn(template_name="wiawdp/contract_table_actions.html", orderable=False)

    def render_client(self, value):
        return f'{value.first_name} {value.last_name} ({value.pk})'

    class Meta:
        model = Contract
        template_name = 'django_tables2/bootstrap.html'
        fields = ('row_pks', 'pk', 'client', 'workforce', 'end_date', 'performance')


class WIAWDPTable(tables.Table):
    class Meta:
        model = WIAWDP
        template_name = 'django_tables2/bootstrap.html'
        exclude = ('id',)

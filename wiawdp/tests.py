from django.contrib.auth.models import User

from wiawdp.models import Workforce, Contract


def create_workforce(workforce):
    return Workforce.objects.create(workforce=workforce)


def create_contract(client, workforce, end_date, performance):
    return Contract.objects.create(client=client, workforce=workforce, end_date=end_date, performance=performance)


def login_as_admin(test_case):
    test_case.admin = User.objects.get(username='admin')
    test_case.client.force_login(test_case.admin)

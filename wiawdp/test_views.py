from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone, dateformat

from students.models import Student
from wiawdp.models import Workforce, Contract
from wiawdp.views import AddContractView


def create_user(username, email, password, is_active=True, is_staff=False, is_superuser=False):
    return User.objects.create_user(username=username, email=email, password=password, is_active=is_active,
                               is_staff=is_staff,
                               is_superuser=is_superuser)


def create_admin():
    return create_user('admin', '', '', True, True, True)


def create_student(id, first_name, last_name, ssn, zip_code, city, cell_phone, email, location, refer, sources):
    return Student.objects.create(id=id, first_name=first_name, last_name=last_name, ssn=ssn, zipcode=zip_code,
                                  city=city,
                                  cellPhone=cell_phone, email=email, location=location, refer=refer, sources=sources)


def create_workforce(workforce):
    return Workforce.objects.create(workforce=workforce)


def create_contract(client, workforce, end_date, performance):
    return Contract.objects.create(client=client, workforce=workforce, end_date=end_date, performance=performance)


def create_and_login_as_admin(test_case):
    test_case.admin = create_admin()
    test_case.client.force_login(test_case.admin)


class ContractViewTestCase(TestCase):
    def setUp(self):
        create_and_login_as_admin(self)

    def test_default_redirect(self):
        response = self.client.get(reverse('wiawdp:contracts'))
        self.assertRedirects(response, f'{reverse("wiawdp:contracts")}?status=active')

    def test_filter_active(self):
        response = self.client.get(reverse('wiawdp:contracts'), data={'status': 'active'})
        self.assertEqual(response.status_code, 200)

    def test_filter_inactive(self):
        response = self.client.get(reverse('wiawdp:contracts'), data={'status': 'inactive'})
        self.assertEqual(response.status_code, 200)

    def test_filter_blank(self):
        response = self.client.get(reverse('wiawdp:contracts'), data={'status': ''})
        self.assertEqual(response.status_code, 200)


class AddContractViewTestCase(TestCase):
    def setUp(self):
        self.admin = create_admin()
        self.client.force_login(self.admin)
        self.student = create_student(0, 'Name', 'Surname', '000000000', '00000', 'City', '+18888888888',
                                      'someone@example.com', 'Location', 'refer', '')
        self.workforce = create_workforce('work force')

    def test_post_filled_form(self):
        data = {
            'client': self.student.pk,
            'workforce': self.workforce.pk,
            'end_date': dateformat.format(timezone.now(), 'Y-m-d H:i:s'),
            'performance': 5
        }

        response = self.client.post(reverse('wiawdp:add_contract'), data)
        self.assertRedirects(response, AddContractView.success_url, fetch_redirect_response=False)


class SearchContractsViewTestCase(TestCase):
    def setUp(self):
        self.admin = create_admin()
        self.client.force_login(self.admin)

    def test_post_filled_form(self):
        data = {
            'first_name': 'first',
            'last_name': 'last',
            'ssn': '000000000',
            'email': 'someone@example.com',
            'cell_phone': '+18888888888',
            'zipcode': '00000'
        }

        response = self.client.post(reverse('wiawdp:search_contracts'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wiawdp/search_contracts_results.html')


class ModifyContractViewTestCase(TestCase):
    def setUp(self):
        self.admin = create_admin()
        self.client.force_login(self.admin)
        self.student = create_student(0, 'Name', 'Surname', '000000000', '00000', 'City', '+18888888888',
                                      'someone@example.com', 'Location', 'refer', '')
        self.end_date = timezone.now()
        self.workforce = create_workforce('Red')
        self.performance = '5'
        self.contract = create_contract(self.student, self.workforce, self.end_date, self.performance)

    def test_post_filled_form(self):
        updated_end_date = self.contract.end_date + timezone.timedelta(days=1)
        updated_end_date_str = dateformat.format(updated_end_date, 'Y-m-d H:i:s')
        updated_workforce = create_workforce('Green')
        updated_performance = 3

        data = {
            'end_date': updated_end_date_str,
            'workforce': updated_workforce.pk,
            'performance': updated_performance
        }

        response = self.client.post(f'{reverse("wiawdp:modify_contract")}?contract_id={self.contract.pk}', data)
        updated_contract = Contract.objects.get(pk=self.contract.pk)
        self.assertRedirects(response, reverse('wiawdp:contracts'), fetch_redirect_response=False)
        self.assertGreater(updated_contract.end_date, self.contract.end_date)
        self.assertEqual(updated_contract.workforce, updated_workforce)
        self.assertEqual(updated_contract.performance, updated_performance)


class ModifyContractLookupViewTestCase(TestCase):
    def setUp(self):
        self.admin = create_admin()
        self.client.force_login(self.admin)

    def test_post_filled_form(self):
        response = self.client.post(reverse('wiawdp:modify_contract_lookup'), {'student_id': 0})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wiawdp/modify_contract_lookup_results.html')


class DeleteContractViewTestCase(TestCase):
    def setUp(self):
        self.admin = create_user('admin', 'admin@avtech.com', 'avtech123', True, True, True)
        self.student = create_student(0, 'John', 'Doe', '888888888', '88888', 'City', '8888888888', 'email@email.com',
                                      'ABC Town',
                                      'ref', 'source')
        create_workforce('Red')
        create_workforce('Green')
        create_workforce('Blue')

        self.client.force_login(self.admin)

    def test_delete_none(self):
        workforce = Workforce.objects.get(workforce='Red')
        create_contract(self.student, workforce, timezone.now(), 1)

        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': []})
        self.assertEqual(Contract.objects.count(), 1)

    def test_delete_single(self):
        workforce = Workforce.objects.get(workforce='Red')
        c_1 = create_contract(self.student, workforce, timezone.now(), 1)
        create_contract(self.student, workforce, timezone.now(), 2)
        create_contract(self.student, workforce, timezone.now(), 3)
        create_contract(self.student, workforce, timezone.now(), 3)
        create_contract(self.student, workforce, timezone.now(), 5)

        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': [c_1.pk]})
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_1.pk)
        self.assertEqual(Contract.objects.count(), 4)

    def test_delete_multiple(self):
        workforce = Workforce.objects.get(workforce='Red')
        c_1 = create_contract(self.student, workforce, timezone.now(), 1)
        c_2 = create_contract(self.student, workforce, timezone.now(), 2)
        c_3 = create_contract(self.student, workforce, timezone.now(), 3)
        create_contract(self.student, workforce, timezone.now(), 3)
        create_contract(self.student, workforce, timezone.now(), 5)

        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': [c_1.pk, c_2.pk, c_3.pk]})
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_1.pk)
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_2.pk)
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_3.pk)
        self.assertEqual(Contract.objects.count(), 2)

    def test_delete_nonexistant(self):
        workforce = Workforce.objects.get(workforce='Red')
        create_contract(self.student, workforce, timezone.now(), 1)

        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': [100]})
        self.assertEqual(Contract.objects.count(), 1)

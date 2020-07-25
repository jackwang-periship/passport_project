from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone, dateformat

from students.models import Student
from wiawdp.models import Workforce, Contract
from wiawdp.views import AddContractView
from wiawdp.tests import login_as_admin


class ContractViewTestCase(TestCase):
    fixtures = ['user.json']

    def setUp(self):
        login_as_admin(self)

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
    fixtures = ['student.json', 'user.json', 'workforce.json']

    def setUp(self):
        login_as_admin(self)
        self.student = Student.objects.get(pk=1)
        self.workforce = Workforce.objects.get(pk=1)

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
    fixtures = ['user.json']

    def setUp(self):
        login_as_admin(self)

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
    fixtures = ['contract.json', 'student.json', 'user.json', 'workforce.json']

    def setUp(self):
        login_as_admin(self)
        self.student = Student.objects.get(pk=1)
        self.end_date = timezone.now()
        self.workforce = Workforce.objects.get(pk=1)
        self.performance = 5
        self.contract = Contract.objects.get(pk=1)

    def test_post_filled_form(self):
        updated_end_date = self.contract.end_date + timezone.timedelta(days=1)
        updated_end_date_str = dateformat.format(updated_end_date, 'Y-m-d H:i:s')
        updated_workforce = Workforce.objects.get(pk=2)
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
    fixtures = ['user.json']

    def setUp(self):
        login_as_admin(self)

    def test_post_filled_form(self):
        response = self.client.post(reverse('wiawdp:modify_contract_lookup'), {'student_id': 0})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wiawdp/modify_contract_lookup_results.html')


class DeleteContractViewTestCase(TestCase):
    fixtures = ['contract.json', 'student.json', 'user.json', 'workforce.json']

    def setUp(self):
        login_as_admin(self)
        self.student = Student.objects.get(pk=1)
        self.initial_num_contracts = Contract.objects.count()

    def test_delete_none(self):
        num_contracts = Contract.objects.count()
        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': []})
        self.assertEqual(Contract.objects.count(), num_contracts)

    def test_delete_single(self):
        c_1 = Contract.objects.get(pk=1)

        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': [c_1.pk]})
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_1.pk)
        self.assertEqual(Contract.objects.count(), self.initial_num_contracts - 1)

    def test_delete_multiple(self):
        c_1 = Contract.objects.get(pk=1)
        c_2 = Contract.objects.get(pk=2)
        c_3 = Contract.objects.get(pk=3)

        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': [c_1.pk, c_2.pk, c_3.pk]})
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_1.pk)
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_2.pk)
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_3.pk)
        self.assertEqual(Contract.objects.count(), self.initial_num_contracts - 3)

    def test_delete_nonexistant(self):
        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': [100]})
        self.assertEqual(Contract.objects.count(), self.initial_num_contracts)

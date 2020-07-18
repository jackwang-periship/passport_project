from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from wiawdp.models import Contract, Workforce
from students.models import Student
from django.contrib.auth.models import User


def create_user(username, email, password, is_active=True, is_staff=False, is_superuser=False):
    return User.objects.create(username=username, email=email, password=password, is_active=is_active,
                               is_staff=is_staff,
                               is_superuser=is_superuser)


def create_student(id, first_name, last_name, ssn, zip_code, city, cell_phone, email, location, refer, sources):
    return Student.objects.create(id=id, first_name=first_name, last_name=last_name, ssn=ssn, zipcode=zip_code,
                                  city=city,
                                  cellPhone=cell_phone, email=email, location=location, refer=refer, sources=sources)


def create_workforce(work_force):
    return Workforce.objects.create(workforce=work_force)


def create_contract(client, workforce, end_date, performance):
    return Contract.objects.create(client=client, workforce=workforce, end_date=end_date, performance=performance)


class DeleteContractViewTests(TestCase):
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
        work_force = Workforce.objects.get(workforce='Red')
        create_contract(self.student, work_force, timezone.now(), 1)

        response = self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': []})
        print(response.status_code)
        self.assertEqual(Contract.objects.count(), 1)

    def test_delete_single(self):
        work_force = Workforce.objects.get(workforce='Red')
        c_1 = create_contract(self.student, work_force, timezone.now(), 1)
        create_contract(self.student, work_force, timezone.now(), 2)
        create_contract(self.student, work_force, timezone.now(), 3)
        create_contract(self.student, work_force, timezone.now(), 3)
        create_contract(self.student, work_force, timezone.now(), 5)

        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': [c_1.pk]})
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_1.pk)
        self.assertEqual(Contract.objects.count(), 4)

    def test_delete_multiple(self):
        work_force = Workforce.objects.get(workforce='Red')
        c_1 = create_contract(self.student, work_force, timezone.now(), 1)
        c_2 = create_contract(self.student, work_force, timezone.now(), 2)
        c_3 = create_contract(self.student, work_force, timezone.now(), 3)
        create_contract(self.student, work_force, timezone.now(), 3)
        create_contract(self.student, work_force, timezone.now(), 5)

        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': [c_1.pk, c_2.pk, c_3.pk]})
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_1.pk)
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_2.pk)
        self.assertRaises(Contract.DoesNotExist, Contract.objects.get, pk=c_3.pk)
        self.assertEqual(Contract.objects.count(), 2)

    def test_delete_nonexistant(self):
        work_force = Workforce.objects.get(workforce='Red')
        create_contract(self.student, work_force, timezone.now(), 1)

        self.client.post(reverse('wiawdp:delete_contracts'), {'row_pks': [100]})
        self.assertEqual(Contract.objects.count(), 1)

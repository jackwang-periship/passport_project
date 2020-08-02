from django.core.exceptions import ValidationError
from django.test import TestCase
from wiawdp.forms import FindStudentForm


class FindStudentFormTestCase(TestCase):
    def test_no_change(self):
        form = FindStudentForm()
        self.assertFalse(form.is_valid())

    def test_empty(self):
        form = FindStudentForm(data={})
        self.assertFalse(form.is_valid())

    def test_completely_filled(self):
        data = {
            'first_name': 'first',
            'last_name': 'last',
            'ssn': '000000000',
            'email': 'someone@example.com',
            'cell_phone': '+18888888888',
            'zipcode': '00000'
        }
        form = FindStudentForm(data=data)
        self.assertTrue(form.is_valid(), f'Form Errors: {form.errors.as_data()}')

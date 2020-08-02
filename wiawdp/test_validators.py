from django.core.exceptions import ValidationError
from unittest import TestCase
from wiawdp.validators import SSNValidator, ZIPCodeValidator


class SSNValidatorTestCase(TestCase):
    validator = SSNValidator()

    def test_no_hyphens(self):
        try:
            self.validator('000000000')
        except ValidationError:
            self.fail()

    def test_two_hyphens(self):
        try:
            self.validator('000-00-0000')
        except ValidationError:
            self.fail()

    def test_only_first_hyphen(self):
        self.assertRaises(ValidationError, self.validator, '000-000000')

    def test_only_second_hyphen(self):
        self.assertRaises(ValidationError, self.validator, '00000-0000')

    def test_hyphens_wrong_place(self):
        self.assertRaises(ValidationError, self.validator, '0-0000-0000')

    def test_empty(self):
        self.assertRaises(ValidationError, self.validator, '')

    def test_too_short(self):
        self.assertRaises(ValidationError, self.validator, '0')

    def test_too_long(self):
        self.assertRaises(ValidationError, self.validator, '0000000000')

    def test_alpha_chars(self):
        self.assertRaises(ValidationError, self.validator, 'aaaaaaaaa')


class ZIPCodeValidatorTestCase(TestCase):
    validator = ZIPCodeValidator()

    def test_proper_length(self):
        try:
            self.validator('00000')
        except ValidationError:
            self.fail()

    def test_empty(self):
        self.assertRaises(ValidationError, self.validator, '')

    def test_too_short(self):
        self.assertRaises(ValidationError, self.validator, '0')

    def test_too_long(self):
        self.assertRaises(ValidationError, self.validator, '000000')

    def test_non_numeric(self):
        self.assertRaises(ValidationError, self.validator, 'aaaaa')

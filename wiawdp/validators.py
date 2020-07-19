from django.core.validators import RegexValidator


class SSNValidator(RegexValidator):
    regex = r'\d{3,}-?\d{2,}-?\d{4,}'
    message = 'Please enter a valid SSN.'


class ZIPCodeValidator(RegexValidator):
    regex = r'\d{5,}'
    message = 'Please enter a valid ZIP code.'

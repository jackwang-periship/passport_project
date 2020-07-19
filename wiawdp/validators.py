from django.core.validators import RegexValidator

ssn_validator = RegexValidator(r'\d{3,}-?\d{2,}-?\d{4,}', 'Please enter a valid SSN')

zip_code_validator = RegexValidator(r'\d{5,}', 'Please enter a valid ZIP code.')

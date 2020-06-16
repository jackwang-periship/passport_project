from django.db import models
# from pclients.models import Pclient
import uuid
from django.contrib.auth.models import User

class Address(models.Model):
    address = models.CharField(max_length=50)
    ext_address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
    country = models.CharField(max_length=50, default="US")

    # class Meta:
    #     verbose_name = 'Paddress'
    #     verbose_name_plural = 'Paddress'

    def __str__(self):
        return f'{self.address}, {self.city}, {self.state}'
        # return self.address + self.city + self.state

# Same as Pclient except with ssn, cell_phone, and home_phone added in
class Person(models.Model):
    MR = 'Mr'
    MRS = 'Mrs'
    MS = 'Ms'
    NONE = 'None'
    SALUTATION = (
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MS, 'Ms'),
        (NONE, 'None'),
    )
    uuid = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    desc = models.TextField(blank=True)
    home_phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    title = models.CharField(max_length=32)
    salutation = models.CharField(max_length=8, choices=SALUTATION, default=NONE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        # verbose_name_plural = 'pclient'
        ordering = ['created_on']

    def __str__(self):
        return self.last_name + self.first_name
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # def get_absolute_url(self):
    #     return reverse('model-detail-view', args=[str(self.id)])
    #
    # def get_update_url(self):
    #     return 'pclient_update', [self.uuid]
    #
    # def get_delete_url(self):
    #     return 'pclient_delete', [self.uuid]

class Workforce(models.Model):
    workforce = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.workforce



class Contract(models.Model):
    # STATUS_CHOICES = [
    #     ('ACTIVE', 'Active'),
    #     ('INACTIVE', 'Inactive')
    # ]
    client = models.ForeignKey(Person, on_delete=models.CASCADE)
    workforce = models.ForeignKey(Workforce, null=True, on_delete=models.CASCADE)
    end_date = models.DateTimeField()
    performance = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.client} - {self.workforce} - {self.end_date}'
    # status = models.CharField(max_length=8, choices=STATUS_CHOICES)


class CareerPathway(models.Model):
    career_pathway = models.CharField(max_length=200)
    cip_code = models.CharField(max_length=7)
    program_title = models.CharField(max_length=200)
    date_approved = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.program_title} - {self.location} ({self.cip_code})'



# class Location(models.Model):
#     location = models.CharField(max_length=200, unique=True)
#
#     def __str__(self):
#         return self.location
#     class Meta:
#         ordering = ['location']

# class Student(models.Model):
#     GENDER_CHOICES = [
#         ('MALE', 'Male'),
#         ('FEMALE', 'Female')
#     ]
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     ssn = models.CharField(max_length=9)
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

# us_states = [
#     ('AK', 'Alaska'),
#     ('AL', 'Alabama'),
#     ('AR', 'Arkansas'),
#     ('AS', 'American Samoa'),
#     ('AZ', 'Arizona'),
#     ('CA', 'California'),
#     ('CO', 'Colorado'),
#     ('CT', 'Connecticut'),
#     ('DC', 'District of Columbia'),
#     ('DE', 'Delaware'),
#     ('FL', 'Florida'),
#     ('GA', 'Georgia'),
#     ('GU', 'Guam'),
#     ('HI', 'Hawaii'),
#     ('IA', 'Iowa'),
#     ('ID', 'Idaho'),
#     ('IL', 'Illinois'),
#     ('IN', 'Indiana'),
#     ('KS', 'Kansas'),
#     ('KY', 'Kentucky'),
#     ('LA', 'Louisiana'),
#     ('MA', 'Massachusetts'),
#     ('MD', 'Maryland'),
#     ('ME', 'Maine'),
#     ('MI', 'Michigan'),
#     ('MN', 'Minnesota'),
#     ('MO', 'Missouri'),
#     ('MP', 'Northern Mariana Islands'),
#     ('MS', 'Mississippi'),
#     ('MT', 'Montana'),
#     ('NA', 'National'),
#     ('NC', 'North Carolina'),
#     ('ND', 'North Dakota'),
#     ('NE', 'Nebraska'),
#     ('NH', 'New Hampshire'),
#     ('NJ', 'New Jersey'),
#     ('NM', 'New Mexico'),
#     ('NV', 'Nevada'),
#     ('NY', 'New York'),
#     ('OH', 'Ohio'),
#     ('OK', 'Oklahoma'),
#     ('OR', 'Oregon'),
#     ('PA', 'Pennsylvania'),
#     ('PR', 'Puerto Rico'),
#     ('RI', 'Rhode Island'),
#     ('SC', 'South Carolina'),
#     ('SD', 'South Dakota'),
#     ('TN', 'Tennessee'),
#     ('TX', 'Texas'),
#     ('UT', 'Utah'),
#     ('VA', 'Virginia'),
#     ('VI', 'Virgin Islands'),
#     ('VT', 'Vermont'),
#     ('WA', 'Washington'),
#     ('WI', 'Wisconsin'),
#     ('WV', 'West Virginia'),
#     ('WY', 'Wyoming')
# ]
# class Address(models.Model):
#     address = models.CharField(max_length=50)
#     ext_address = models.CharField(max_length=50, blank=True)
#     city = models.CharField(max_length=60)
#     state = models.CharField(max_length=2, choices=us_states)
#     zipcode = models.CharField(max_length=5)
#     country = models.CharField(max_length=50, default="US")

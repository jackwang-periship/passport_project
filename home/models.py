from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from phonenumber_field.modelfields import PhoneNumberField

USER_ROLE_CHOICES = [
    ('student', 'Student'),
    ('prospective', 'Prospective '),
    ('avtechemployee', 'AVTech Employee'),
    ('instructor', 'Instructor'),
    ('instructor_contractor', 'Instructor - Adjunct'),
    ('vendor_institutional', 'Vendor - Institutional'),
    ('vendor_government', 'Vendor - Government'),
    ('vendor_business', 'Vendor - Business'),
]

AVTECH_DEPARTMENT_CHOICES = [
    ('administration', 'Administration'),
    ('admission', 'Admission'),
    ('marketing', 'Marketing'),
    ('sales', 'Sales'),
    ('humanresources', 'Human Resources'),
    ('careerservices', 'Career Services'),
    ('finance', 'Finannce'),
    ('staff', 'Staff'),
    ('faculty', 'Faculty'),
]


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    role = models.CharField(max_length=32, choices=USER_ROLE_CHOICES)
    avtech_department = models.CharField(max_length=32, choices=AVTECH_DEPARTMENT_CHOICES)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('home:userprofile-detail', kwargs={'pk' : self.id})

    class Meta:
        permissions = (("can_list_userprofiles", "List All User Profiles"),)

class Address(models.Model):
    address = models.CharField(max_length=50)
    ext_address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30, null=True, blank=True)
    zip_code = models.CharField(max_length=5, null=True, blank=True)
    country = models.CharField(max_length=50, default="US")

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.address}, {self.city}, {self.state} {self.zip_code}'


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
    home_phone = PhoneNumberField(null=True, blank=True)
    cell_phone = PhoneNumberField()
    email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=32)
    salutation = models.CharField(max_length=8, choices=SALUTATION, default=NONE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from courses.models import LOCATION_CHOICES


class Student(models.Model):
    YES = 'Yes'
    NO = 'No'
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    Chooses = (
        (YES, 'Yes'),
        (NO, 'No'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=11, help_text='example:123-45-6789 (dash is included automatically')
    zipcode = models.CharField(max_length=10, help_text='example: 99999')
    address = models.CharField(max_length=30)
    country = models.CharField(max_length=50, default="United States of America")
    city = models.CharField(max_length=30)
    cellPhone = PhoneNumberField(help_text='example: +12125552368')
    email = models.EmailField(max_length=30)
    location = models.CharField(max_length=30, choices=LOCATION_CHOICES, default='southplainfield-g')
    refer = models.CharField(max_length=30, blank=True, help_text='Not Required')
    sources = models.CharField(max_length=30, blank=True, help_text='Not Required')
    gender = models.CharField(max_length=10, choices=GENDER, default=MALE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ['created_on']

    def __str__(self):
        return self.last_name + self.first_name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def get_update_url(self):
        return 'student_update', [self.uuid]

    def get_delete_url(self):
        return 'student_delete', [self.uuid]

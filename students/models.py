from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


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
    ssn = models.CharField(max_length=9)
    zipcode = models.CharField(max_length=5)
    country = models.CharField(max_length=50, default="United States of America")
    city = models.CharField(max_length=30)
    cellPhone = PhoneNumberField(required=False)
    homePhone = PhoneNumberField(required=False)
    email = models.CharField(max_length=30)
    location = models.CharField(max_length=30, required=False)
    refer = models.CharField(max_length=30, default="No Refer", required=False)
    sources = models.CharField(max_length=30, default="Individual", required=False)
    notes = models.CharField(max_length=200, required= False)
    gender = models.CharField(max_length=10, choices=GENDER, default=MALE)
    newsLetter = models.TextField(required= False)
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

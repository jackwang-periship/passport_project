from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from pclients.models import Paddress


USER_TYPE_CHOICES = [
    ('student', 'Student'),
    ('avtechemployee', 'AVTech Employee'),
    ('instructor', 'Instructor'),
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

AVTECH_EMPLOYEE_ROLE_CHOICES = [
    ('instructor', 'Instructor'),
    ('instructor_contractor', 'Adjunct Instructor'),
    ('careerservices', 'Career Services'),
    ('technology', 'Technology'),
    ('staff', 'Staff'),
    ('humanresources', 'Human Resources'),
    ('admission', 'Admission'),
]


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    type = models.CharField(max_length=32, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=32, choices=AVTECH_DEPARTMENT_CHOICES)
    role = models.CharField(max_length=32, choices=AVTECH_EMPLOYEE_ROLE_CHOICES)

    class Meta:
        permissions = (("can_list_employees", "List All Employees"),)

    def __str__(self):
        """String for representing the Model object."""
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('home:employee-detail', args=[str(self.id)])

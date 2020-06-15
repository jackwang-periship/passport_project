from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from pclients.models import Paddress

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


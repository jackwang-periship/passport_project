from django.db import models
from django.contrib.auth.models import User
from students.models import Student


class Workforce(models.Model):
    workforce = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.workforce


class Contract(models.Model):
    # STATUS_CHOICES = [
    #     ('ACTIVE', 'Active'),
    #     ('INACTIVE', 'Inactive')
    # ]
    client = models.ForeignKey(Student, on_delete=models.CASCADE)
    workforce = models.ForeignKey(Workforce, null=True, on_delete=models.CASCADE)
    end_date = models.DateTimeField()
    performance = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.client} - {self.workforce} - {self.end_date}'
    # status = models.CharField(max_length=8, choices=STATUS_CHOICES)


class WIAWDP(models.Model):
    career_pathway = models.CharField(max_length=200)
    cip_code = models.CharField(max_length=7)
    program_title = models.CharField(max_length=200)
    date_approved = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.program_title} - {self.location} ({self.cip_code})'

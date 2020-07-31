from django.db import models
from django.contrib.auth.models import User
from students.models import Student


class Workforce(models.Model):
    workforce = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.workforce


PERFORMANCE_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
]
class Contract(models.Model):
    client = models.ForeignKey(Student, on_delete=models.CASCADE)
    workforce = models.ForeignKey(Workforce, null=True, on_delete=models.CASCADE)
    end_date = models.DateTimeField()
    performance = models.IntegerField(null=True, blank=True, choices=PERFORMANCE_CHOICES)

    def __str__(self):
        return f'{self.client} - {self.workforce} - {self.end_date}'


class WIAWDP(models.Model):
    EATONTOWN = 'EATONTOWN'
    FAIRFIELD = 'FAIRFIELD'
    SOUTH_PLAINFIELD = 'SOUTH_PLAINFIELD'
    LOCATION_CHOICES = [
        (EATONTOWN, 'Eatontown'),
        (FAIRFIELD, 'Fairfield'),
        (SOUTH_PLAINFIELD, 'South Plainfield')
    ]
    career_pathway = models.CharField(max_length=200)
    cip_code = models.CharField(max_length=7)
    program_title = models.CharField(max_length=200)
    date_approved = models.DateField()
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    # start_date = models.DateField(null=True, blank=True)
    # end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.program_title} - {self.location} ({self.cip_code})'

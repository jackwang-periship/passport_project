from django.db import models

# Create your models here.
class Schedule(models.Model):
    id = models.IntegerField(primary_key= True)
    course_name = models.CharField(max_length=64)
    location = models.CharField(max_length= 16)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    hours = models.DecimalField(max_digits=4, decimal_places=2)
    instructor = models.CharField(max_length=64)
    approved = models.BooleanField(default=False)

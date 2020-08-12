
from django.db import models

# Create your models here.
from django.db.models import DateTimeField


class Attendances(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Instructor = models.CharField(max_length=30)
    timeStamp = models.DateTimeField()

    # def save(self, *args, **kwargs):
    #     super(Attendances, self).save(*args, **kwargs)

    def __str__(self):
        return self.last_name + ", " + self.first_name

    class Meta:
        verbose_name = ('Attendance')
        verbose_name_plural = ('Attendances')
        # permissions = (("can_list_courses", "List All The Courses"),)

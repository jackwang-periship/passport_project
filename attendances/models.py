from django.db import models
from courses.models import Course
from students.models import Student
# Create your models here.

'''
    The module django.utils is used in the variable timeStamp who value is equal to models.DateTimeFiled with the parameter(timezone.now).
'''
from django.utils import timezone
from datetime import date

#Used on the line where timeStamp = models.DateTimeField(date.today)
from datetime import datetime

class Attendances(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    Instructor = models.CharField(max_length=30) #Check
    #timeStamp = models.DateTimeField(date.today, timezone.now) #timeStamp
    timeStamp = models.DateTimeField(default=datetime.now)
    course = models.ForeignKey(Course, on_delete=models.PROTECT) #Check
    last_name = Student.last_name
    # def save(self, *args, **kwargs):
    #     super(Attendances, self).save(*args, **kwargs)

    def __str__(self):
        return self.course.name

    class Meta:
        verbose_name = ('Attendance')
        verbose_name_plural = ('Attendances')
        # permissions = (("can_list_courses", "List All The Courses"),)


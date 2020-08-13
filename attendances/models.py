from django.db import models
from courses.models import Course
from students.models import Student
# Create your models here.
from django.db.models import DateTimeField


class Attendances(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    Instructor = models.CharField(max_length=30)
    timeStamp = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    # def save(self, *args, **kwargs):
    #     super(Attendances, self).save(*args, **kwargs)

    def __str__(self):
        return self.course.name + ", " + self.student.first_name + " " + self.student.last_name

    class Meta:
        verbose_name = ('Attendance')
        verbose_name_plural = ('Attendances')
        # permissions = (("can_list_courses", "List All The Courses"),)

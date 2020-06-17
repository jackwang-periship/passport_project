from django.db import models
from django.utils import timezone
# from django.template.defaultfilters import slugify

# Any Changes
# python manage.py makemigrations
# python manage.py migrate

# python manage.py shell
# from transaction.models import Transaction
# Transaction.objects.all()
# Transaction.objects.create()

# Create your models here.
class VerifiedId(models.Model):
    studentId = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.studentId)

class Transaction(models.Model):
    # verifiedId = models.ForeignKey(VerifiedId, on_delete=models.PROTECT)
    verifiedId = models.PositiveIntegerField()
    firstName = models.CharField(max_length=14)
    lastName = models.CharField(max_length=18)
    counselor = models.CharField(max_length=24)
    course = models.CharField(max_length=32)
    balance = models.DecimalField(max_digits=8,decimal_places=2)
    date = models.DateField(default=timezone.now)
    # slug = models.SlugField(unique=true)

    # def save(self, *args, **kwargs):
    #   self.slug = slugify(self.name)
    #   super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return str(self.verifiedId) + "-" + str(self.date)


class Report(models.Model):

    TYPE_CHOICES = (
        ("payment", "By Payment"),
        ("location", "By Location"),
        ("counselor", "By Counselor"),
        ("course", "By Course"),
    )

    startD = models.DateField(default=timezone.now)
    endD = models.DateField(default=timezone.now)
    type = models.CharField(max_length=12, choices=TYPE_CHOICES, default='Choose Type')
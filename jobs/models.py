from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    company = models.CharField(max_length=64, verbose_name="Company")
    contactName = models.CharField(max_length=64, verbose_name="Contact Name")
    contactEmail = models.EmailField(verbose_name="Contact Email")
    companyAddress = models.CharField(max_length=64, verbose_name="Company Address")
    class Meta:
        verbose_name = ('jobs_client')
        verbose_name_plural = ('jobs_clients')


class Posting(models.Model):
    title = models.CharField(max_length=64, verbose_name="Course")
    location = models.CharField(max_length=64, verbose_name="Location")
    deadline = models.DateField(verbose_name="Deadline")
    postedDate = models.DateField(auto_now_add=True, verbose_name="Posted Date")
    position = models.CharField(max_length=64, verbose_name="Position")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')

class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='applicant_user')
    posting = models.ForeignKey(Posting, on_delete=models.PROTECT, related_name='posting')
    class Meta:
        permissions = (('can_apply', 'Can Apply'),)


class CompanyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='user_company')
    class Meta:
        permissions = (('company_user', 'Company User'),)

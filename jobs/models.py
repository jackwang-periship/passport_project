from django.db import models

# Create your models here.
class Client(models.Model):
    company = models.CharField(max_length=64, verbose_name="Company")
    contactName = models.CharField(max_length=64, verbose_name="Contact Name")
    contactEmail = models.EmailField(verbose_name="Contact Email")
    companyAddress = models.CharField(max_length=64, verbose_name="Company Address")
    class Meta:
        verbose_name = ('jobs_client')
        verbose_name_plural = ('jobs_clients')
        permissions = (("can_edit_postings", "Edit Postings"),)

class Posting(models.Model):
    title = models.CharField(max_length=64, verbose_name="Course")
    location = models.CharField(max_length=64, verbose_name="Location")
    deadline = models.DateField(verbose_name="Deadline")
    postedDate = models.DateField(auto_now_add=True, verbose_name="Posted Date")
    position = models.CharField(max_length=64, verbose_name="Position")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')

class Applicant(models.Model):
    name = models.CharField(max_length=64)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='posting')

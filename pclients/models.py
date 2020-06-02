import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Paddress(models.Model):
    address = models.CharField(max_length=50)
    ext_address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
    country = models.CharField(max_length=50, default="US")

    class Meta:
        verbose_name = 'Paddress'
        verbose_name_plural = 'Paddress'

    def __str__(self):
        return self.address + self.city + self.state


class Pclient(models.Model):
    MR = 'Mr'
    MRS = 'Mrs'
    MS = 'Ms'
    NONE = 'None'
    SALUTATION = (
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MS, 'Ms'),
        (NONE, 'None'),
    )
    uuid = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    desc = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    title = models.CharField(max_length=32)
    salutation = models.CharField(max_length=8, choices=SALUTATION, default=NONE)
    address = models.ForeignKey(Paddress, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'pclient'
        ordering = ['created_on']

    def __str__(self):
        return self.last_name + self.first_name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def get_update_url(self):
        return 'pclient_update', [self.uuid]

    def get_delete_url(self):
        return 'pclient_delete', [self.uuid]

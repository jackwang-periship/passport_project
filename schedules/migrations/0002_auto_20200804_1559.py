# Generated by Django 3.0.6 on 2020-08-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='location',
            field=models.CharField(max_length=32),
        ),
    ]
# Generated by Django 3.0.6 on 2020-06-23 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20200622_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'permissions': (('can_view_pending_schedule', 'Can View Pending Schedule'),)},
        ),
    ]

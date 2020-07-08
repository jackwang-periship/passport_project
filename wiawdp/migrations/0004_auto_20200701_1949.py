# Generated by Django 3.0.6 on 2020-07-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiawdp', '0003_auto_20200616_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='performance',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='wiawdp',
            name='location',
            field=models.CharField(choices=[('EATONTOWN', 'Eatontown'), ('FAIRFIELD', 'Fairfield'), ('SOUTH_PLAINFIELD', 'South Plainfield')], max_length=200),
        ),
    ]

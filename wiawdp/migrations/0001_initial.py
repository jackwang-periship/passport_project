# Generated by Django 3.0.6 on 2020-08-04 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WIAWDP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_pathway', models.CharField(max_length=200)),
                ('cip_code', models.CharField(max_length=7)),
                ('program_title', models.CharField(max_length=200)),
                ('date_approved', models.DateField()),
                ('location', models.CharField(choices=[('EATONTOWN', 'Eatontown'), ('FAIRFIELD', 'Fairfield'), ('SOUTH_PLAINFIELD', 'South Plainfield')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workforce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workforce', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateTimeField()),
                ('performance', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('workforce', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wiawdp.Workforce')),
            ],
        ),
    ]

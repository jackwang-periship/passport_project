# Generated by Django 3.0.6 on 2020-08-13 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instructor', models.CharField(max_length=30)),
                ('timeStamp', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.Student')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
            },
        ),
    ]
from django.db import models
from home.models import UserProfile
from django.template.defaultfilters import slugify

LOCATION_CHOICES = [
    ('southplainfield-g', 'South Plainfield G'),
    ('southplainfield-b', 'South Plainfield B'),
    ('southplainfield-c', 'South Plainfield C'),
    ('southplainfield-d', 'South Plainfield D'),
    ('southplainfield-e', 'South Plainfield E'),
    ('southplainfield-a', 'South Plainfield A'),
    ('southplainfield-h', 'South Plainfield H'),
    ('southplainfield-f', 'South Plainfield F'),
    ('fairfield-e', 'Fairfield E'),
    ('fairfield-a', 'Fairfield A'),
    ('fairfield-b', 'Fairfield B'),
    ('fairfield-c', 'Fairfield C'),
    ('fairfield-d', 'Fairfield D'),
    ('eatontown-a', 'Eatontown A'),
    ('eatontown-b', 'Eatontown B'),
    ('eatontown-c', 'Eatontown C'),
    ('eatontown-d', 'Eatontown D'),
    ('eatontown-e', 'Eatontown E'),
]

SUBJECT_CHOICES = [
    ('medical_tech', 'Medical Tech'),
    ('dental', 'Detal'),
    ('programming', 'Computer Programming'),
    ('security', 'Security'),
    ('database', 'Database'),
    ('project_management', 'Project Management'),
]


class Student(models.Model):
    user_profile = models.ForeignKey(UserProfile, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user_profile.user.username


class Counselor(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, on_delete=models.DO_NOTHING)


class WIAWDP(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=70, help_text="Please enter the course name.")
    subject = models.CharField(max_length=32, choices=SUBJECT_CHOICES)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    student = models.ManyToManyField('Student', null=True, blank=True, related_name=('Student'))
    counselor = models.ManyToManyField('Counselor', null=True, blank=True, related_name=('Counselor'))
    wiawdp = models.OneToOneField('WIAWDP', null=True, blank=True, related_name=('WIAWDP'), on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=32, choices=LOCATION_CHOICES)
    permissions = (("can_list_courses", "List All The Courses"),)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('course')
        verbose_name_plural = ('courses')
        ordering = ['-created']
        permissions = (("can_list_courses", "List All The Courses"),)

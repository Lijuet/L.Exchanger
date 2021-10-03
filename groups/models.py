from django.db import models
from django.db.models.fields import IntegerField, PositiveSmallIntegerField

# Create your models here.
class Group(models.Model):
    # num_members = models.PositiveSmallIntegerField()
    # array field for member
    group_name = models.CharField(max_length=30, default="study group")
    is_recruiting = models.BooleanField(default=True)
    # is_active = models.BooleanField()
    # study_start_time = models.TimeField()
    # study_hour = models.TimeField() 
    # study_DOW = models.CharField()
    # array field for study language

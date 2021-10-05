from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields.related import ForeignKey

from accounts.models import User

# Create your models here.
class Group(models.Model):
    
    LANGUAGE_CHOICES={
        ("ko", "Korean"),
        ("en", "English"),
    }

    group_name = models.CharField(max_length=30, default="study group")
    is_recruiting = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    study_languages = ArrayField(models.CharField(max_length=3, choices=LANGUAGE_CHOICES), null=True)
    

class GroupMember(models.Model):
    group_id = ForeignKey(Group, on_delete=models.CASCADE, db_column="group_id")
    member_id = ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
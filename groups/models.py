from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields.related import ForeignKey

from accounts.models import User

# Create your models here.
class GroupManager(models.Manager):
    def create_group(self, group_name, study_languages, wish_members, **extra_fields):
        group = self.model(
            group_name=group_name,
            study_languages=study_languages,
            )
        
        group.is_recruiting = True
        group.is_active = True
        group.save(using=self._db)

        self.create_group_members(group, wish_members)
        return group
    

    def create_group_members(self, group, wish_members):
        for member_email in wish_members:
            group_member = GroupMember(group_id=group, member_id=User.objects.get_or_create(email=member_email)[0])
            group_member.save(using=self._db)


class Group(models.Model):
    
    LANGUAGE_CHOICES={
        ("ko", "Korean"),
        ("en", "English"),
    }

    group_name = models.CharField(max_length=30, default="study group")
    is_recruiting = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    study_languages = ArrayField(models.CharField(max_length=3, choices=LANGUAGE_CHOICES), null=True)

    objects = GroupManager()
    

class GroupMember(models.Model):
    group_id = ForeignKey(Group, on_delete=models.CASCADE, db_column="group_id")
    member_id = ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
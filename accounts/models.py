from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password, main_language, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=email,
            username=username,
            main_language=main_language)
        
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, main_language, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        user = self.create_user(
            email=email,
            username=username,
            password=password,
            main_language=main_language,
            **extra_fields)

        user.is_admin = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    
    LANGUAGE_CHOICES={
        ("ko", "Korean"),
        ("en", "English"),
    }
    GOAL_CHOICES={
        ("conv", "Conversation"),
        ("test", "Test"),
    }
    
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="Email",
    )

    username = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="User Name"
    )

    main_language = models.CharField(
        max_length=3,
        choices=LANGUAGE_CHOICES,
        verbose_name="Main Language",
        default="ko"
    )

    study_language = models.CharField(
        max_length=3,
        choices=LANGUAGE_CHOICES,
        verbose_name="Study Language",
        default="en"
    )

    goal = models.CharField(
        max_length=4,
        choices=GOAL_CHOICES,
        verbose_name="Goal",
        default="conv"
    )

    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'main_language']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

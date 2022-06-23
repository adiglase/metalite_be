from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, username, full_name, password, gender, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(email, username, full_name, password, gender, **other_fields)

    def create_user(self, email, username, full_name, password, gender, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, full_name=full_name, gender=gender, **other_fields)
        user.set_password(password)
        user.save()
        return user


GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female')
)

username_validator = RegexValidator(regex=r'^\S*$', message='Username should not included with space',
                                    code='invalid_username')


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', unique=True)
    username = models.CharField(max_length=50, unique=True, validators=[username_validator])
    full_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name', 'gender']

    def __str__(self):
        return self.username

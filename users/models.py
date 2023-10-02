from wsgiref.validate import validator


from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=32 , unique=True,help_text= _('Required 30 characters or fewer starting with a letter, Letters, digits') )
    validators = [validators.RegexValidator]


class UserProfile(models.Model):
    user = models.OneToOneField()

from email.policy import default
from enum import unique
from operator import truediv
from tabnanny import verbose
from time import timezone
from tracemalloc import is_tracing
from wsgiref.validate import validator


from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
# from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager,send_mail



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, phone_number, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number,
                          username=username, email= email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)

        if not extra_fields.get('no_password'):
            user.set_password(password)

        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=32 , unique=True,help_text= _('Required 30 characters or fewer starting with a letter, Letters, digits') ,
                                validators = [validators.RegexValidator(r'^[a-zA-Z][a-zA-Z0-9_\.]+$]',_('Enter a valid sure name starting with a-z.'),'invalid'),] ,
                                error_messages={'unique': _("A user with that username already exist.")},)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True, null=True , blank=True)
    phone_number = models.BigIntegerField(_('mobile number'), unique=True, null=True, blank=True,
                                          validators=[validators.RegexValidator(r'^989[0-3,9]\d{8}$',('Enter a valid mobile number.'),)] ,
                                          error_messages={'unique': _("A user with this mobile number already exists.")} 
                                            )
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_seen = models.DateTimeField(_('last seen date'), null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name , self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_loggedin_user(self):
        return self.phone_number is not None or self.email is not None

    def save(self, *args, **kwargs):
        if self.email is not None and self.email.strip() == '':
            self.email = None
        super().save(*args, **kwargs)



# class UserProfile(models.Model):
#     user = models.OneToOneField()

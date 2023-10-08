from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


from .models import User, Province


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields' : ('username', 'password')}),
        (_('Personal info'), {'fields' : ('first_name', 'last_name', 'phone_number', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staf', 'is_superuser','groups', 'user_permissions')}),
        (_('Important dates'), {'fields' : ('last_login', 'date_joined')}),
    )


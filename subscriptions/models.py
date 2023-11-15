from django.db import models
from django.utils.translation import ugettext_lazy as _


# from 

class Package(models.Model):
    title = models.CharField(_('title'), max_length=50)
    sku = models.CharField(_('stock keeping unit'), max_length=20, validators=[validate_sku], db_index=True)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='packages/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    price = models.PositiveIntegerField(_('price'))
    duration =  models.DurationField(_('duration'), blank=True, null = True)
    created_time = models.DateTimeField (_('created time'), auto_now_add=True)
    updateed_time = models.DateTimeField(_('update time'), auto_now=True)

    class Meta:
        db_table = 'packages'
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')


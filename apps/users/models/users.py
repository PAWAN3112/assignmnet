from generics.models import GenericModel
from django.db import models
from django_enumfield.enum import EnumField
from django.utils.translation import ugettext_lazy as _


class User(GenericModel):
    name = models.CharField(max_length=32)
    email = models.EmailField(_('email address'), max_length=254, null=True, blank=True)
    mobile_number = models.CharField(_('mobile number'), max_length=12, unique=True)

    def __str__(self):
        return "{}:{}".format(self.id, self.name)

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')


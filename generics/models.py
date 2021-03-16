from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings


class GenericModel(models.Model):
    created_on = models.DateTimeField(
        _("Created At"),
        auto_now_add=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='+',
        null=True
    )

    updated_on = models.DateTimeField(
        _("Modified At"),
        auto_now=True,
        db_index=True
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='+',
        null=True
    )

    is_active = models.BooleanField(
        _("Is Instance marked Active"),
        default=True,
        db_index=True
    )

    class Meta:
        abstract = True

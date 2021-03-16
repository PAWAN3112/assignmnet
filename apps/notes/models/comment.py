from generics.models import GenericModel
from django.db import models
from django_enumfield.enum import EnumField
from django.utils.translation import ugettext_lazy as _

from apps.notes.enum import CommentHeirarchy
from apps.users.models import User


class Comment(GenericModel):
    comments = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    commented_by = models.ForeignKey(User, related_name='comment_user', on_delete=models.PROTECT)
    comment_date = models.DateField()
    modified_by = models.ForeignKey(User, related_name='modified_user', on_delete=models.PROTECT, null=True, blank=True)
    modified_on = models.DateField(null=True, blank=True)
    comment_heirarchy = EnumField(CommentHeirarchy, default=CommentHeirarchy.INDIVIDUAL)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        db_table = 'notes_comment'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


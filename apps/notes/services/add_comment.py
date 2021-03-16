# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.notes.models import Comment


class AddCommentService(object):

    def add_comment(self, **kwargs):
        comments = kwargs.get('comments')
        parent_comment_id = kwargs.get('parent_comment_id')
        commented_by = kwargs.get('commented_by')
        comment_date = kwargs.get('comment_date')
        modified_by = kwargs.get('modified_by')
        modified_on = kwargs.get('modified_on')
        comment_heirarchy = kwargs.get('comment_heirarchy', 1)

        assert commented_by, 'User Field is required.'
        assert comments, 'comment Field is required.'

        comment_obj = Comment(
            comments=comments,
            parent_comment_id=parent_comment_id,
            commented_by_id=commented_by,
            comment_date=comment_date,
            modified_by=modified_by,
            modified_on=modified_on,
            comment_heirarchy=comment_heirarchy
        )
        return comment_obj

    def update_comment(self, instance, **kwargs):
        instance.comments = kwargs.get('comments')
        instance.modified_by_id = kwargs.get('modified_by')
        instance.modified_on = kwargs.get('modified_on')
        return instance

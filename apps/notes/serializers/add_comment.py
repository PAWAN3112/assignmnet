# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.conf import settings
from rest_framework import serializers
from apps.users.models import User


from apps.notes.models import Comment

from apps.users.serializers.user import UserField


class AddCommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    commented_by = UserField(required=False)
    comment_date = serializers.DateField(required=False)
    parent_id = serializers.IntegerField(required=False)
    modified_by = UserField(required=False)
    modified_on = serializers.DateField(required=False)

    def validate(self, data):
        if self.context.method != 'PUT':
            if not data.get('comment_date') or not data.get('commented_by'):
                raise serializers.ValidationError('Comment Date or Commented by is missing')
            user_obj = User.objects.filter(id=data.get('commented_by')).first()
            if not user_obj:
                raise serializers.ValidationError('This user is not present')
        else:
            if not data.get('modified_by') or not data.get('modified_on') or not data.get('id'):
                raise serializers.ValidationError('Modified Date or Modified by or id is missing')
            user_obj = User.objects.filter(id=data.get('modified_by')).first()
            if not user_obj:
                raise serializers.ValidationError('This user is not present')
        return data

    class Meta:
        model = Comment
        fields = (
            '__all__'
        )

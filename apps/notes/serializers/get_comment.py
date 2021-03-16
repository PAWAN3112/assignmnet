from __future__ import unicode_literals

from rest_framework import serializers

from apps.notes.models import Comment
from apps.users.serializers.user import UserPublicSerializer

from apps.users.serializers.user import UserField


class GetCommentSerializer(serializers.ModelSerializer):
    commented_by = UserField()
    modified_by = UserField()

    class Meta:
        model = Comment
        fields = (
            '__all__'
        )

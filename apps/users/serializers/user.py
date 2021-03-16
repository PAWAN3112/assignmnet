from __future__ import unicode_literals

from rest_framework import serializers
from apps.users.models import User


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'mobile_number', 'email')


class UserField(serializers.Field):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return UserPublicSerializer(value).data

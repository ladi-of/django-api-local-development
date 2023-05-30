from rest_framework import serializers
from .models import UserSpec


class UserSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSpec
        fields = ['id', 'username']

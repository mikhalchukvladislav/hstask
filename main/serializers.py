from rest_framework import serializers
from .models import Auth, InviteCode


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = '__all__'


class InviteCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InviteCode
        fields = '__all__'
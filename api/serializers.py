from rest_framework import serializers
from auth_app.models import Userplus, InviteCode


class SendActivationCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)


class ActivateUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    activation_code = serializers.CharField(max_length=4)


class EnterInviteCodeSerializer(serializers.Serializer):
    invite_code = serializers.CharField(max_length=6)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userplus
        fields = ['phone_number', 'invite_code', 'activated_invite_code']

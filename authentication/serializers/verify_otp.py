from rest_framework import serializers

from authentication.models import CustomUser

class VerifyOTPSerializer(serializers.ModelSerializer):

  class Meta:
    model = CustomUser
    fields = ('email', 'otp',)

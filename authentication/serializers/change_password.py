from rest_framework import serializers  

from authentication.models import CustomUser

class ChangePasswordSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('otp_code', 'password', 'email')
    readonly_fields = ('password',)

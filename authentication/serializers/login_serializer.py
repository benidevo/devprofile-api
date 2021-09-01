from rest_framework import serializers

from authentication.models import CustomUser

class LoginSerializer(serializers.ModelSerializer):
  password = serializers.CharField(max_length=9)

  class Meta:
    model = CustomUser
    fields = ('email', 'password')

from rest_framework import serializers

from authentication.models import CustomUser

class ResetPasswordSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('email',)

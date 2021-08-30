from rest_framework import serializers

from authentication.models import CustomUser

class VerifyTokenSerializer(serializers.ModelSerializer):

  class Meta:
    model = CustomUser
    fields = ('token')

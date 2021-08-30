from rest_framework import serializers

from authentication.models import CustomUser

class SignUpSerializer(serializers.ModelSerializer):

  class Meta:
    model = CustomUser
    fields = ('first_name', 'last_name', 'company_name', 'email',)

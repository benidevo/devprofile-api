from rest_framework import serializers

from authentication.models import CustomUser

class SignUpSerializer(serializers.ModelSerializer):
  '''
  Register a new user
  '''

  class Meta:
    model = CustomUser
    fields = ('first_name', 'last_name', 'company_name', 'email', 'role',)

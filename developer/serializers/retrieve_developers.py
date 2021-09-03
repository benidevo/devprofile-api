from developer.models import DeveloperProfile
from authentication.models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = CustomUser
    fields = ('id', 'first_name', 'last_name', 'token',)
 

class RetrieveDevelopersSerializer(serializers.ModelSerializer):
  user = UserSerializer()

  class Meta:
    model = DeveloperProfile
    fields = ('id', 'about', 'languages', 'projects', 'phone_number', 'email', 'user')
 
from developer.models import DeveloperProfile, Project
from authentication.models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = CustomUser
    fields = ('id', 'first_name', 'last_name', 'token',)

class ProjectSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields = ('id', 'title', 'description', 'url',)
 

class RetrieveDevelopersSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  projects = ProjectSerializer(many=True)

  class Meta:
    model = DeveloperProfile
    fields = ('id', 'about', 'languages', 'experience', 'projects', 'phone_number', 'email', 'stack', 'user',)
 
from rest_framework import serializers

from developer.models import DeveloperProfile, Project

class ProjectSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields =  ('id', 'title', 'description', 'url',)

class DeveloperProfileSerializer(serializers.ModelSerializer):
  projects = ProjectSerializer()

  class Meta:
    model = DeveloperProfile
    # exclude = ('user',)
    fields = ('about', 'phone_number', 'languages', 'projects',)
    extra_kwargs = {"about": {"required": False}, "phone_number": {"required": False}, "languages": {"required": False}, "projects": {"required": False}}
    

from rest_framework import serializers

from developer.models import DeveloperProfile, Project

class ProjectSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields =  ('id', 'title', 'description', 'url',)
    extra_kwargs = {"title": {"required": False}, "description": {"required": False}, "url": {"required": False}}


class DeveloperProfileSerializer(serializers.ModelSerializer):
  projects = ProjectSerializer()

  class Meta:
    model = DeveloperProfile
    fields = ('about', 'phone_number', 'languages', 'experience', 'projects')
    extra_kwargs = {"about": {"required": False}, "phone_number": {"required": False}, "languages": {"required": False},  "experience": {"required": False}, "projects": {"required": False}}

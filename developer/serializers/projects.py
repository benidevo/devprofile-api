from rest_framework import serializers

from developer.models import Project 

class ProjectSerializer(serializers.ModelSerializer):
 
  class Meta:
    model = Project
    fields =  ('id', 'title', 'description', 'url', 'image',)
    extra_kwargs = {"title": {"required": False}, "description": {"required": False}, "url": {"required": False}, "image": {"required": False}}

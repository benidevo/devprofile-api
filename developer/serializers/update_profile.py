from rest_framework import serializers

from developer.models import DeveloperProfile

class DeveloperProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = DeveloperProfile
    fields = ('about', 'phone_number', 'languages', 'experience', 'stack',)
    extra_kwargs = {"about": {"required": False}, "phone_number": {"required": False}, "languages": {"required": False},  "experience": {"required": False}, "stack": {"required": False}}


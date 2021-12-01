from pyexpat import model
from authentication.models import CustomUser
from rest_framework import serializers

from recruiter.models import RecruiterProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'company_name',)


class RecruiterProfileSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = RecruiterProfile
        fields = ('id', 'user', 'user_detail', 'image',
                  'about', 'phone_number', 'email')
        extra_kwargs = {'image': {'required': False}, 'id': {'read_only': True}, 'phone_number': {
            'required': False}, 'email': {'read_only': True}, 'about': {'required': False}}
        # read_only_fields = ('id', 'user', 'image')

from rest_framework import status, generics

from recruiter.models import RecruiterProfile
from recruiter.serializers.profile_serializer import RecruiterProfileSerializer
from utils.response import Response


class RecruiterProfileView(generics.GenericAPIView):

    serializer_class = RecruiterProfileSerializer

    def get(self, request):
        '''
        Retrieve a recruiter profiles
        '''
        recruiters = RecruiterProfile.objects.filter(user=request.user).first()
        if not recruiters:
            return Response(errors={'message': 'Invalid Authentication credentials'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(recruiters)
        if not serializer.is_valid:
            return Response(errors={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'recruiter': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        '''
        Update a recruiter's profile
        '''
        recruiter = RecruiterProfile.objects.filter(user=request.user).first()
        about = request.data.get('about')
        company_name = request.data.get('company_name')
        phone_number = request.data.get('phone_number')

        if company_name:
            recruiter.user.company_name = company_name
            recruiter.user.save()
        if phone_number:
            recruiter.phone_number = phone_number
        if about:
            recruiter.about = about

        recruiter.save()
        serializer = self.serializer_class(recruiter)
        return Response(data={'recruiter': serializer.data}, status=status.HTTP_201_CREATED)

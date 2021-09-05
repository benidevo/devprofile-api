from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework import status, generics, permissions
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from utils.response import Response
from developer.permissions import IsOwnerOrReadOnly

from developer.models import DeveloperProfile, Project
from authentication.models import CustomUser
from developer.serializers.update_profile import DeveloperProfileSerializer
from developer.serializers.retrieve_developers import RetrieveDevelopersSerializer, ProjectSerializer

class DeveloperProfileView(generics.GenericAPIView):
  
  serializer_class = DeveloperProfileSerializer
  parser_classes = (MultiPartParser, JSONParser, FormParser)
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


  def get_queryset(self):
    queryset = DeveloperProfile.objects.all()

    # search title by text
    dev = self.request.query_params.get('dev', None)
    if dev is not None:
      queryset = queryset.filter(user__first_name__iexact=dev)
      return queryset

    # filter by type
    stack = self.request.query_params.get('stack', None)
    if stack is not None:
      queryset = queryset.filter(stack=stack.upper())
      return queryset

    return queryset

  def put(self, request):
    '''
    Update developer profile 
    '''
    user_data = request.data
    serializer = self.serializer_class(data=user_data, partial=True)
    about = user_data.get('about', '')    
    avatar = user_data.get('avatar', '')    
    phone_number = user_data.get('phone_number', '')    
    languages = user_data.get('languages', '')
    experience = user_data.get('experience', '')
    stack = user_data.get('stack', '')

    if not serializer.is_valid():
      return Response(errors=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
      developerProfile = DeveloperProfile.objects.get(user=request.user)
    except:
      return Response(errors={'message': 'User does not exist'}, status=status.HTTP_204_NO_CONTENT)


    if about:
      developerProfile.about = about
    if phone_number:
      developerProfile.phone_number = phone_number
    if languages:
      developerProfile.languages = languages
    if experience:
      developerProfile.experience = experience
    if stack:
      developerProfile.stack = stack.upper()
    
    developerProfile.user = request.user
    
    developerProfile.save()

    return Response(data={'message': 'Profile created successfully'}, status=status.HTTP_204_NO_CONTENT)



    if settings.USE_S3:
      developerProfile = DeveloperProfile(avatar=avatar)
      developerProfile.save()
      avatar_url = developerProfile.avatar.url
      return Response(data={'message': avatar_url}, status=status.HTTP_401_UNAUTHORIZED)
    else:
      fs = FileSystemStorage()
      filename = fs.save('image1', avatar)
      avatar_url = fs.url(filename)
      return Response(data={'message': avatar_url}, status=status.HTTP_401_UNAUTHORIZED)

    # return Response(errors={'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
  def get(self, request):
    '''
    Retrieve a list of all the developers \n \nQuery params include:\n?dev=<developer's first name> \n?stack=<developer's stack>
    '''
    developers = self.get_queryset()
    serializer = RetrieveDevelopersSerializer(developers, many=True)
    if serializer.is_valid:
      return Response(data={'developers': serializer.data}, status=status.HTTP_200_OK)



class DeveloperProfileByIDView(generics.GenericAPIView):
  
  serializer_class = DeveloperProfileSerializer
  parser_classes = (MultiPartParser, JSONParser, FormParser)
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

  def get(self, request, id):
    '''
    Retrieve a developer profile with a provided ID
    '''
    try:
      developer = DeveloperProfile.objects.get(pk=id)
    except:
      return Response(errors={'developers': 'Found no developer with the provided ID'}, status=status.HTTP_404_NOT_FOUND)

    serializer = RetrieveDevelopersSerializer(developer)
    if serializer.is_valid:
      return Response(data={'developer': serializer.data}, status=status.HTTP_200_OK)

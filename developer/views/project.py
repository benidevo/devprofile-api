from functools import partial
import re
from developer import serializers
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework import status, generics, permissions
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from utils.response import Response
from developer.permissions import IsOwnerOrReadOnly

from developer.models import DeveloperProfile, Project
from authentication.models import CustomUser
from developer.serializers.update_profile import DeveloperProfileSerializer
from developer.serializers.projects import ProjectSerializer


class ProjectView(generics.GenericAPIView):

  serializer_class = ProjectSerializer
  parser_classes = (MultiPartParser, JSONParser, FormParser)
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

  def post(self, request):
    '''
    Add a new project
    '''
    user_data = request.data
    serializer = self.serializer_class(data=user_data)
    title = user_data.get('title', '')    
    description = user_data.get('description', '')    
    url = user_data.get('url', '')    
    image = user_data.get('image', '')

    if not serializer.is_valid():
      return Response(errors=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    try:
      developer = DeveloperProfile.objects.get(user=request.user)
    except:
      return Response(errors={'message': 'Invalid Authentication Credentials. You\'r not a registered user.'}, status=status.HTTP_401_UNAUTHORIZED)

    Project.objects.create(developer=developer, title=title, description=description, url=url)
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
  
    




  def get(self, request):
    '''
    Retrieve a list of all the projects associated with the authenticated Developer's profile
    '''
    try:
      developer = DeveloperProfile.objects.get(user=request.user)
    except:
      return Response(errors={'message': 'Invalid Authentication Credentials. You\'r not a registered user.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
      projects = Project.objects.filter(developer=developer)
    except:
      return Response(errors={'me': ''}, status=status.HTTP_401_UNAUTHORIZED)
    print(projects)
    serializer = self.serializer_class(projects, many=True).data
    
    return Response(data={'projects': serializer}, status=status.HTTP_200_OK)


class EditProjectView(generics.GenericAPIView):

  serializer_class = ProjectSerializer
  parser_classes = (MultiPartParser, JSONParser, FormParser)
  # permission_classes = (

  def put(self, request, id):
    '''
    Edit project
    '''
    user_data = request.data
    serializer = self.serializer_class(data=user_data, partial=True)
    url = user_data.get('url', '')
    title = user_data.get('title', '')
    description = user_data.get('description', '')

    if not serializer.is_valid():
      return Response(errors=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
      project = Project.objects.get(pk=id)
    except:
      return Response(errors={'message': 'No project with the provided ID'}, status=status.HTTP_404_NOT_FOUND)
    
    if url:
      project.url = url
    if title:
      project.title = title
    if description:
      project.description = description
    project.save()

    return Response(data=serializer.data, status=status.HTTP_200_OK)

  def delete(self, request, id):
    '''
    Delete a project using the provided ID
    '''
    try:
      project = Project.objects.get(pk=id)
    except:
      return Response(errors={'message': 'No project with the provided ID'}, status=status.HTTP_404_NOT_FOUND)

    project.delete()

    return Response(data={'message': 'Successfully deleted project'}, status=status.HTTP_200_OK)
import os
import uuid
from django.db import models
from django.conf import settings
from django.utils.deconstruct import deconstructible

@deconstructible
class GenerateProfileImagePath(object):

  def __init__(self,):
    pass

  def __call__(self, instance, filename):
    ext = filename.split('.')[-1]
    path = f'media/accounts/{instance.user.id}/images'
    name = f'profile_images/.{ext}'
    return os.path.join(path, name)

avatar_path = GenerateProfileImagePath()
  
class DeveloperProfile(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='developer_user')
  avatar = models.FileField(upload_to=avatar_path)
  about = models.TextField()
  languages = models.TextField()
  phone_number = models.CharField(max_length=20)
  experience = models.CharField(max_length=50, null=True)
  email = models.EmailField(unique=True)
  stack = models.CharField(max_length=100, null=True)

  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}\'s Profile'
    

class Project(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  title = models.CharField(max_length=100, null=True)
  description = models.TextField(null=True)
  url = models.URLField(null=True)
  image = models.FileField(null=True, blank=True)
  developer = models.ForeignKey(DeveloperProfile, null=True, on_delete=models.DO_NOTHING, related_name='projects')

  def __str__(self):
    return self.title
    
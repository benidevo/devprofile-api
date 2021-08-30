import uuid
from django.db import models
from django.conf import settings

# Create your models here.
class DeveloperProfile(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='developer_user')
  about = models.TextField()
  languages = models.TextField()
  projects = models.TextField()
  phone_number = models.CharField(max_length=20)

  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}\'s Profile'

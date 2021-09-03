import uuid
from django.db import models
from django.conf import settings

class RecruiterProfile(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recruiter_user')
  about = models.TextField()
  phone_number = models.CharField(max_length=20)
  email = models.EmailField(unique=True)

  def __str__(self):
    return f'{self.user.company_name}\'s Profile'

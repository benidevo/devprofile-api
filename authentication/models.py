import uuid
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
  """
  Custom user model manager where email is the unique identifiers
  for authentication instead of usernames.
  """
  def create_user(self, email, password, **extra_fields):
    """
    Create and save a User with the given email and password.
    """
    if not email:
      raise ValueError(_('The Email must be set'))
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password, **extra_fields):
    """
    Create and save a SuperUser with the given email and password.
    """
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError(_('Superuser must have is_staff=True.'))
    if extra_fields.get('is_superuser') is not True:
      raise ValueError(_('Superuser must have is_superuser=True.'))
    return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  username = None
  first_name = models.CharField(max_length=50, blank=True, null=True)
  last_name = models.CharField(max_length=50, blank=True, null=True)
  company_name = models.CharField(max_length=200, blank=True, null=True)
  email = models.EmailField(_('email address'), unique=True)
  is_developer = models.BooleanField(default=True)
  is_recruiter = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  otp_code = models.CharField(max_length=50)
  role = models.CharField(max_length=50, default='developer')
  date_joined = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return f'{self.first_name} {self.last_name}' if not self.company_name else f'{self.company_name}'
    
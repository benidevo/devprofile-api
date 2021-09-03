from django.contrib import admin

from developer.models import DeveloperProfile, Project

# Register your models here.
admin.site.register(DeveloperProfile)
admin.site.register(Project)
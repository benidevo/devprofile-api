from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from developer.views.update_profile import DeveloperProfileView, DeveloperProfileByIDView
from developer.views.project import ProjectView, EditAndDeleteProjectView

urlpatterns = [
  path('profile', csrf_exempt(DeveloperProfileView.as_view()), name='developers'),
  path('profile/<id>', csrf_exempt(DeveloperProfileByIDView.as_view()), name='developers'),
  path('projects', csrf_exempt(ProjectView.as_view()), name='developers-projects'),
  path('projects/<id>', csrf_exempt(EditAndDeleteProjectView.as_view()), name='developers-projects'),
]

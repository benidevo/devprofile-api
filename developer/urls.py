from django.urls import path

from developer.views.update_profile import DeveloperProfileView, DeveloperProfileByIDView
from developer.views.project import ProjectView, EditAndDeleteProjectView

urlpatterns = [
  path('profile', DeveloperProfileView.as_view(), name='developers'),
  path('profile/<id>', DeveloperProfileByIDView.as_view(), name='developers'),
  path('projects', ProjectView.as_view(), name='developers-projects'),
  path('projects/<id>', EditAndDeleteProjectView.as_view(), name='developers-projects'),
]

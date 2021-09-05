from django.urls import path

from developer.views.update_profile import DeveloperProfileView, DeveloperProfileByIDView
from developer.views.project import ProjectView, EditProjectView

urlpatterns = [
  path('', DeveloperProfileView.as_view(), name='developers'),
  path('<id>', DeveloperProfileByIDView.as_view(), name='developers'),
  path('projects', ProjectView.as_view(), name='developers-projects'),
  path('projects/<id>', EditProjectView.as_view(), name='developers-projects'),
]

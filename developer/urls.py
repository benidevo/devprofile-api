from django.urls import path

from developer.views.create_profile import DeveloperProfileView

urlpatterns = [
  path('', DeveloperProfileView.as_view(), name='developers'),
  # path('all', AllDevs.as_view(), name='developers-list'),
]
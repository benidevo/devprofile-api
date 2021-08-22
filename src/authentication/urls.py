from django.urls import path

from authentication.views import TestView

urlpatterns = [
  path('', TestView.as_view(), name='test')
]

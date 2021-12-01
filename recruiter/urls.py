from django.urls import path

from recruiter.views.recruiter_profile import RecruiterProfileView

urlpatterns = [
    path('profile', RecruiterProfileView.as_view(), name='recruiter_profile')
]

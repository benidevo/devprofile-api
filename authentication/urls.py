from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from authentication.views.reset_password import ResetPassword

from authentication.views.signup import SignUp
from authentication.views.login import Login
from authentication.views.verify_otp import VerifyOTP
from authentication.views.reset_password import ResetPassword
from authentication.views.change_password import ChangePassword

urlpatterns = [
  path('change-password', csrf_exempt(ChangePassword.as_view()), name='change-password'),
  path('reset-password', csrf_exempt(ResetPassword.as_view()), name='reset-password'),
  path('login', csrf_exempt(Login.as_view()), name='login'),
  path('verify-otp', csrf_exempt(VerifyOTP.as_view()), name='verify-otp'),
  path('signup', csrf_exempt(SignUp.as_view()), name='signup'),
]

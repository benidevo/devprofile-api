from django.urls import path
from authentication.views.reset_password import ResetPassword

from authentication.views.signup import SignUp
from authentication.views.login import Login
from authentication.views.verify_otp import VerifyOTP
from authentication.views.reset_password import ResetPassword
from authentication.views.change_password import ChangePassword

urlpatterns = [
  path('change-password', ChangePassword.as_view(), name='change-password'),
  path('reset-password', ResetPassword.as_view(), name='reset-password'),
  path('login', Login.as_view(), name='login'),
  path('verify-otp', VerifyOTP.as_view(), name='verify-otp'),
  path('signup', SignUp.as_view(), name='signup'),
]

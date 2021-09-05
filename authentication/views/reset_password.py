from authentication.models import CustomUser
from rest_framework import status, generics
from utils.Utils import Mailer

from utils.response import Response
from authentication.serializers.reset_password import ResetPasswordSerializer
from authentication.serializers.change_password import ChangePasswordSerializer
from authentication.views.signup import generate_key

class ResetPassword(generics.GenericAPIView):
  '''
  Generates otp to reset user password.
  '''
  serializer_class = ResetPasswordSerializer

  def post(self, request):
    user_data = request.data
    serializer = self.serializer_class(data=user_data)
    email = user_data.get('email', '')

    try:
      user = CustomUser.objects.get(email=email)
    except:
      return Response(errors={'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    
    otp = generate_key(6)
    user.is_active = False
    user.otp = otp
    user.save()

    # send user email
    email_body = f'''We are sorry you can't access your account. Kindly reset your password with this otp:  {otp}'''
    data = {'email_body': email_body, 'to_email': [
      email], 'email_subject': 'Reset Password'}

    # Send email
    is_email_sent = Mailer.send_email(data)
    if not is_email_sent:
      return Response(
          errors=dict(
              email_error='Email service is unavailable, please try later'),
          status=status.HTTP_503_SERVICE_UNAVAILABLE
      )
    return Response(data=dict(email=email, otp=otp), status=status.HTTP_200_OK)


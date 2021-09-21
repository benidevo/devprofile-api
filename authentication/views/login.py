from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.authtoken.models import Token

from utils.response import Response
from authentication.models import CustomUser
from authentication.serializers.login_serializer import LoginSerializer
from utils.Utils import Mailer
from utils.generate_otp import generate_key

class Login(generics.GenericAPIView):
  '''
    Authenticate a user
  '''

  serializer_class = LoginSerializer

  def post(self, request):
    user_data = request.data
    serializer = self.serializer_class(data=user_data)

    email = user_data.get('email', '')
    password = user_data.get('password', '')

    if email == '' or password == '':
      return Response(errors={'invalid_credentials': 'Please provide both email and password'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
      user = CustomUser.objects.get(email=email)
    except:
      return Response(errors={'message': 'User with the provided email does not exist'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not user.is_active:
      # generate new otp
      new_otp = generate_key(6)
      user.otp = new_otp
      user.save()

      email_text = '\n\nIt seems you are yet to activate your account.'
      email_body = f'''Hello, {email_text} Kindly verify your account with this otp:  {user.otp}'''
      data = {'email_body': email_body, 'to_email': [
        email], 'email_subject': 'Account Verification'}

      # Send email
      is_email_sent = Mailer.send_email(data)
      if not is_email_sent:
        return Response(
          errors=dict(email_error='Email service is unavailable, please try later'),
          status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
      return Response(errors={'message': 'Please verify your account before you login', 'otp': user.otp}, status=status.HTTP_401_UNAUTHORIZED)
    
    auth_user = authenticate(username=email, password=password)
    if not auth_user:
      return Response(errors={'message': 'invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=auth_user)
    user_data = {
      'first_name': user.first_name or None,
      'last_name': user.last_name or None,
      'company_name': user.company_name or None,
      'email': user.email,
      'role': user.role
    }
    return Response(data={'token': token.key, 'user': user_data}, status=status.HTTP_200_OK)
    
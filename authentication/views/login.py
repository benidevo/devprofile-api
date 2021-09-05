from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.authtoken.models import Token

from utils.response import Response
from authentication.models import CustomUser
from authentication.serializers.login_serializer import LoginSerializer

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
      return Response(errors={'message': 'Please verify your account'}, status=status.HTTP_400_BAD_REQUEST)
    
    auth_user = authenticate(username=email, password=password)
    if not auth_user:
      return Response(errors={'message': 'invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=auth_user)
    return Response(data={'token': token.key}, status=status.HTTP_200_OK)
    
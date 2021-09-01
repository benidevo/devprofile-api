from rest_framework import status, generics

from utils.response import Response
from authentication.serializers.change_password import ChangePasswordSerializer
from authentication.models import CustomUser

class ChangePassword(generics.GenericAPIView):
  '''
  Change user password
  '''
  serializer_class = ChangePasswordSerializer

  def post(self, request):
    user_data = request.data
    serializer = self.serializer_class(data=user_data)
    token = user_data.get('token', '')
    password = user_data.get('password', '')
    email = user_data.get('email', '')

    if not token:
      return Response(errors={'message': 'Provide a token'}, status=status.HTTP_400_BAD_REQUEST)
      
    if not password:
      return Response(errors={'message': 'Provide a password'}, status=status.HTTP_400_BAD_REQUEST)

    if not email:
      return Response(errors={'message': 'Provide a valid email'}, status=status.HTTP_400_BAD_REQUEST)

    try:
      user = CustomUser.objects.get(email=email)
    except: 
      return Response(errors={'message': 'user with provided email does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if not user.otp_code == token:
      return Response(errors={'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(password)
    user.is_active = True
    user.save()

    return Response(data={'message': 'Password change was successful'}, status=status.HTTP_200_OK)

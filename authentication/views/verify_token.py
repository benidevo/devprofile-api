from rest_framework import status, generics

from utils.response import Response

from authentication.models import CustomUser
from authentication.serializers.verify_token import VerifyTokenSerializer

class VerifyToken(generics.GenericAPIView):
  '''
  Verify the 6 digit auto generated token
  '''
  serializer_class = VerifyTokenSerializer

  def post(self, request):
    user_data = request.data
    serializer = self.serializer_class(data=user_data)
    email = user_data.get('email', '')
    token = user_data.get('token', '')

    if token == '' or email == '':
      return Response(errors={'message': 'Please provide a token and email'}, status=status.HTTP_404_NOT_FOUND)
    
    if not serializer.is_valid():
      return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
      user = CustomUser.objects.get(email=email)
    except:
      return Response(errors={'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if not token == user.otp_code:
      return Response(errors={'message': 'Invalid token'}, status=status.HTTP_404_NOT_FOUND)
    elif token == user.otp_code:
      user.is_active = True
      user.save()
      return Response(data={'message': 'Successfully verified token'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response(errors={'message': 'An unexpected server error occurred'}, status=status.HTTP_404_NOT_FOUND)
    

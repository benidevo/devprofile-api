from rest_framework import status, generics

from utils.response import Response

from authentication.models import CustomUser
from authentication.serializers.verify_otp import VerifyOTPSerializer

class VerifyOTP(generics.GenericAPIView):
  '''
  Verify the 6 digit auto generated otp
  '''
  serializer_class = VerifyOTPSerializer

  def post(self, request):
    user_data = request.data
    serializer = self.serializer_class(data=user_data)
    email = user_data.get('email', '')
    otp = user_data.get('otp', '')

    if otp == '' or email == '':
      return Response(errors={'message': 'Please provide otp and email'}, status=status.HTTP_400_BAD_REQUEST)

    try:
      user = CustomUser.objects.get(email=email)
    except:
      return Response(errors={'message': 'User with the provided email does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if otp != user.otp:
      return Response(errors={'message': 'Invalid otp'}, status=status.HTTP_400_BAD_REQUEST)
    elif otp == user.otp:
      user.is_active = True
      user.save()
      return Response(data={'message': 'Successfully verified otp'}, status=status.HTTP_200_OK)
    
    return Response(errors={'message': 'An unexpected server error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
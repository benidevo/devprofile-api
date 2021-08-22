from rest_framework import status
from rest_framework.views  import APIView
from utils.response import Response

# Create your views here.

class TestView(APIView):
  def get(self, request):
    return Response(data={'news': 'welcome to api'}, status=status.HTTP_200_OK)
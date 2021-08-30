import random
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from authentication.serializers.signup_serializer import SignUpSerializer
from utils.Utils import Mailer
from developer.models import DeveloperProfile
from recruiter.models import RecruiterProfile
from utils.response import Response
from decouple import config


def generate_key(num_digit):
    """Generate key using user email and random str"""
    min_val = 10 ** (num_digit - 1)
    max_val = (10 ** num_digit) - 1
    otp = random.randint(min_val, max_val)
    return otp


class SignUp(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    """Create new user in the system"""
    serializer_class = SignUpSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        first_name = user_data.get('first_name', '')
        last_name = user_data.get('last_name', '')
        company_name = user_data.get('company_name', '')
        role = user_data.get('role', '')
        email = user_data.get('email', '')
        password = user_data.get('password', '')

        if not serializer.is_valid():
            return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # generate token
        otp = generate_key(6)

        # save user insrance
        user = get_user_model().objects.create(first_name=first_name, last_name=last_name, email=email, role=role.lower(), company_name=company_name, password=password)
        user.set_password(password)
        user.otp_code = otp
        if user.role == 'recruiter':
            user.is_recruiter = True
            user.is_developer = False

            recruiter = RecruiterProfile.objects.create(user=user)
            recruiter.save()
            user.save()
            
            email_text = 'Thank you for registering with us. \n\n We are pleased to have you.'
            email_body = f'''Hi {first_name or company_name}, {email_text} Kindly verify your account with this token:  {otp}'''
            data = {'email_body': email_body, 'to_email': [
                email], 'email_subject': 'Account Verification'}

            # Send email
            is_email_sent = Mailer.send_email(data)
            if not is_email_sent:
                return Response(
                    errors=dict(
                        email_error='Email service is unavailable, please try later'),
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )

            return Response(data=dict(company_name=company_name, email=email, otp=otp), status=status.HTTP_201_CREATED)

        developer = DeveloperProfile.objects.create(user=user)
        developer.save()
        user.save()

        return Response(data=dict(first_name=first_name, last_name=last_name, email=email, otp=otp), status=status.HTTP_201_CREATED)
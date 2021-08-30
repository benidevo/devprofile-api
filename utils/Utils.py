from django.core.mail import send_mail
from django.conf import settings

class Mailer:
  @staticmethod
  def send_email(data):
    email_subject=data['email_subject']
    message=data['email_body']
    email_from = settings.EMAIL_HOST_USER
    email_to=data['to_email']
    html_format=data['email_body']
    try:
      send_mail(email_subject, message, email_from, email_to,
      fail_silently=False, html_message=html_format)
      return True;
    except Exception as err:
      print(str(err))
      return False

  @staticmethod
  def validate_image_upload(file):
    return True if file and file.name.split('.')[-1].lower() in ['jpeg','jpg','png','svg'] else False

  @staticmethod
  def validate_video_upload(file):
    return True if file and file.name.split('.')[-1].lower() in ['mp4','avi','flv','mov'] else False
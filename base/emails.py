from django.core.mail import send_mail
from django.conf import settings
def send_account_activation_email(email,email_token):
    
    subject='Validate your account'
    email_from=settings.EMAIL_HOST_USER
    message=f'Hi,click on the link to validate your account http://127.0.0.1:8000/accounts/activate/{email_token}'

    send_mail(subject,message,email_from,[email])
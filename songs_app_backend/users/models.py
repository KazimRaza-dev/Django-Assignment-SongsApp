from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from datetime import datetime


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('enduser', 'End-User'),        # (storedValue, humanReadable value)
        ('admin', 'Admin'),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'password', 'user_type',
                       'first_name', 'last_name')

    def __str__(self):
        return f"{self.username}({self.id})"

    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
        forgot_password_token = "{}".format(reset_password_token.key)
        greetings = "Hi {}!".format(reset_password_token.user.username)

        email_html_content = "<html><body><p>{greetings}</p><p>Please use this Token for password Reset on Songs App:<b> {token}</b></p> <p> The token will expires after 60 minutes.</p><p>If you did not ask to reset your password, please ignore this message.</p></body></html>".format(
            greetings=greetings, token=forgot_password_token)

        message = Mail(
            from_email=os.getenv('EMAIL_SENDER'),
            to_emails=[reset_password_token.user.email],
            subject="Password Reset for {title}".format(title="Songs App. ") +
            str(datetime.now()),
            html_content=email_html_content
        )
        sendgrid_client = SendGridAPIClient(
            api_key=os.getenv('SENDGRID_API_KEY'))
        response = sendgrid_client.send(message)

        if response.status_code == 202:
            print('Password Reset Email sent successfully to ' +
                  str(reset_password_token.user.email))
        else:
            print('Failed to send email')

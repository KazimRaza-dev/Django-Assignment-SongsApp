from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from datetime import datetime


def sendResetPasswordEmail(reset_password_token):
    forgot_password_token = '{}'.format(reset_password_token.key)
    greetings = 'Hi {}!'.format(reset_password_token.user.username)

    email_html_content = '<html><body><p>{greetings}</p><p>Please use this Token for password Reset on Songs App:<b> {token}</b></p> <p> The token will expires after 60 minutes.</p><p>If you did not ask to reset your password, please ignore this message.</p></body></html>'.format(
        greetings=greetings, token=forgot_password_token)

    message = Mail(
        from_email=os.getenv('EMAIL_SENDER'),
        to_emails=[reset_password_token.user.email],
        subject='Password Reset for {title}'.format(title='Songs App. ') +
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

"""
Security util

Will deal with security utility
"""

from itsdangerous import URLSafeTimedSerializer
from flask import current_app
from flask_mail import Message
from app import mail


def generate_confirmation_token(email):
    """
    Generates a confirmation token that the user will use to register
    The actual email is hidden in the token
    :param email: email address of registering user 
    :return: confirmation token
    """
    serializer = URLSafeTimedSerializer(current_app.config.get("SECRET_KEY"))
    return serializer.dumps(email, salt=current_app.config.get("SECURITY_PASSWORD_SALT"))


def confirm_token(token):
    """
    Used to confirm user token during registration process
    :param token: 
    :return: 
    """


def send_email(to, subject, template):
    """
    Sends a confirmation email to registering user
    :param to: who we are sending this email to
    :param subject: subject of email
    :param template: template of the email
    """
    msg = Message(
        subject=subject,
        recipients=[to],
        html=template,
        sender=current_app.config.get("MAIL_DEFAULT_SENDER")
    )
    mail.send(msg)

"""
Security util

Will deal with security utility
"""

from itsdangerous import URLSafeTimedSerializer
from flask import current_app, abort
import hashlib
from datetime import datetime, timedelta
import jwt


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
    we use the loads() method, which takes the token and expiration period
    :param token: token used in registration process
    :return: An email as long as the token has not expired
    """
    serializer = URLSafeTimedSerializer(current_app.config.get("SECRET_KEY"))
    try:
        email = serializer.loads(
            token,
            salt=current_app.config.get("SECURITY_PASSWORD_SALT"),
            max_age=86400  # 24 hours
        )
        return email
    except:
        abort(404)


def generate_auth_token(username, password):
    """
    Generates an auth token given a user's username and password, uses a secret key and
    JWT tokens to generate
    :param username: username of current logged in user
    :param password: password of current logged in user
    :return: JWT string
    :rtype: str
    """
    hash_pass = hashlib.sha512(password.encode("UTF-8")).hexdigest()

    user = dict(username=username,password=hash_pass)
    user['exp'] = datetime.utcnow() + timedelta(minutes=60)
    secret_key = current_app.config.get('SECRET_KEY')
    jwt_string = jwt.encode(user, secret_key)
    return jwt_string.decode("utf-8")
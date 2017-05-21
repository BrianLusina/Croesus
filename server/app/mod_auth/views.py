from . import auth
from flask import jsonify


@auth.route("login", methods=["GET", "POST"])
def login():
    pass


@auth.route("signup", methods=["GET", "POST"])
def signup():
    pass


@auth.route("reset", methods=["GET", "POST"])
def reset_password():
    pass


@auth.route("facebook", methods=["GET", "POST"])
def login_with_facebook():
    """
    Login user with facebook
    """
    pass


@auth.route("google", methods=["GET", "POST"])
def login_with_google():
    """
    Login user with facebook
    """
    pass


@auth.route("twitter", methods=["GET", "POST"])
def login_with_twitter():
    """
    Login user with facebook
    """
    pass

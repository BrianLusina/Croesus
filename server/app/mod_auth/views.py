from . import auth
from .security import generate_confirmation_token, confirm_token
from flask import jsonify, request, redirect, url_for
from app import db
from datetime import datetime
from flask_login import current_user
from .models import UserProfile, UserAccount, UserAccountStatus, FacebookAccount, TwitterAccount, GoogleAccount


@auth.route("register", methods=["GET", "POST"])
def register():
    """
    Registers a new user, get request data, parse it and register user accordingly
    successful registration of user will store data in db and send back a response to client
    informing user to confirm their email account. (An email will be sent for confirmation)
    Thus, afterwards, the user will then confirm their email and the client 
    the client will then redirect user to login and they can proceed to login with their
     registered credentials
    :return: JSON response of the registering user process
    """
    pass


@auth.route('confirm/<token>')
# @login_required
def confirm_email(token):
    """
    Confirm email route for the user. 
    Checks if the user has already confirmed their account
    If they have, log them in. If they have not, 
    confirm their account and direct them to their dashboard we call the confirm_token()
     function, passing in the token. If successful, we update the user,
    changing the email_confirmed attribute to True and setting the datetime for when the 
    confirmation took place.
    Also, in case the user already went through the confirmation process – and is
     confirmed – then we alert the user of this.
    :param token: Generated in the user registration
    :return: A redirect to login
    """

    # if the current user had been confirmed, redirect them to login
    if current_user.confirmed:
        return redirect(url_for('auth.login'))

    # else confirm them
    # get the email for the confirmed
    email = confirm_token(token)

    # get the author or throw an error
    user = UserAccount.query.filter_by(email=current_user.email).first_or_404()

    if user.email == email:
        user.confirmed = True
        user.confirmed_on = datetime.now()

        # update the confirmed_on column
        db.session.add(user)
        db.session.commit()

        # redirect to login
        return redirect(url_for('auth.login'))
    else:
        pass
    # redirect to the user's dashboard
    return redirect(url_for('auth.login'))


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

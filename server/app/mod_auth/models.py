import hashlib
import json
import uuid
from datetime import datetime

from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import Base
from .. import db, login_manager


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class UserAccountStatus(db.Model):
    """
    Stores the user's account status, 0 means the email has not been confirmed, while 1
    means the email has been confirmed
    :cvar __tablename__ name of this model as a table in the db
    :cvar id id of the account status
    :cvar code account status code
    :cvar name account status name
    """
    __tablename__ = "user_account_status"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(40), nullable=False)
    name = Column(String(200), nullable=False)

    def __init__(self, code, name):
        self.code = code
        self.name = name

    user_account = relationship("UserAccount", backref="user_account_status", lazy="dynamic")

    def __repr__(self):
        """
        Create human readable representation of user account status
        :return: string representation of user account status
        """
        return "Id: {}, Code:{}, Name:{}".format(self.id, self.code, self.name)


class UserProfile(Base):
    """
    User profile. This will represent the actual information of the user
    :cvar first_name first name of user
    :cvar last_name user's last name
    :cvar email user's email address
    :cvar accept_tos boolean value indicating user accepts terms of service
    :cvar time_zone user's current timezone
    """
    __tablename__ = "user_profile"

    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    email = Column(String(250), nullable=False, unique=True, index=True)
    accept_tos = Column(Boolean, nullable=False, default=True)
    user_account = relationship("UserAccount", backref="user_profile", lazy="dynamic")

    def from_json(self, user_profile):
        user = json.loads(user_profile)
        self.first_name = user["first_name"]
        self.last_name = user["last_name"]
        self.email = user["email"]
        self.accept_tos = user["accept_tos"]

    def to_json(self):
        return dict(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            date_created=self.date_created,
            date_modified=self.date_modified,
            email=self.email,
            accept_terms_of_service=self.accept_tos,
        )

    def __repr__(self):
        return "FirstName: {first_name}, LastName:{last_name}\n " \
               "Dates:[Created:{date_created}, Modified:{date_modified}]\n " \
               "Email:{email} accept_terms_of_service:{accept_tos}\n".format(
            first_name=self.first_name, last_name=self.last_name,
            date_created=self.date_created, date_modified=self.date_modified,
            email=self.email, accept_tos=self.accept_tos)


class UserAccount(Base, UserMixin):
    """
    User account model
    :cvar uuid unique user id
    :cvar username unique user name of user
    :cvar email email of user
    :cvar email_confirmation_token token for confirming this user
    :cvar password_hash user's hashed password
    :cvar admin boolean indicating if this user is an admin or not

    :cvar user_account_status_id FK id of user account status
    """
    __tablename__ = "user_account"

    uuid = Column(String(250), default=str(uuid.uuid4()), nullable=False)
    username = Column(String(250), nullable=False, unique=True, index=True)
    email = Column(String(250), nullable=False, unique=True, index=True)
    email_confirmation_token = Column(String(350), nullable=True)
    last_seen = Column(DateTime(), default=datetime.now())
    password_hash = Column(String(250), nullable=False)
    admin = Column(Boolean, nullable=True, default=False)
    registered_on = Column(DateTime(), nullable=False, default=datetime.now())
    confirmed = Column(Boolean, nullable=False, default=False)
    confirmed_on = Column(DateTime(), nullable=True)
    avatar_hash = Column(String(32))
    member_since = Column(DateTime(), default=datetime.now)

    user_profile_id = Column(Integer, ForeignKey("user_profile.id"))
    user_account_status_id = Column(Integer, ForeignKey("user_account_status.id"))

    @property
    def registered(self):
        return self.registered_on

    @registered.setter
    def registered(self):
        self.registered_on = datetime.now()

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @password.getter
    def get_password(self):
        return self.password_hash

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_reset_token(self, expiration=3600):
        """
        generates a reset token for this user account
        :param expiration: expiration time,
        :return: reset token
        """
        serializer = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
        return serializer.dumps({"reset": self.id})

    def reset_password(self, token, new_password):
        """
        Resets the user password given reset token and their new password
        :param token: token from generate_reset_token
        :param new_password: new password to reset
        :return: True
        :rtype: bool
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_confirmation_token(self, expiration=3600):
        """
        Generates a confirmation token
        :param expiration: time to expire
        :return: confirmation token
        """
        serializer = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
        self.email_confirmation_token = serializer.dumps({"confirm": self.id})
        return serializer.dumps({"confirm": self.id})

    def confirm_token(self, token):
        """
        Confirms a given token
        :param token: token generated while registering new user
        :return: Boolean
        :rtype: bool
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        """
        Generates email change token
        :param new_email, new users email
        :param expiration: period of time before user's email change token is generated
        :return: generated token for changing email
        """
        serializer = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)

        return serializer.dumps({"change_email": self.id, "new_email": new_email})

    def change_email(self, token):
        """
        Allows the changing of user email given a generated token. This token will be usedd
        to verify that this user is the one authorizing the emeial change
        :param token: generated email change token
        :return: True if email change succeeds, False otherwise
        :rtype: bool
        """
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get("change_email") != self.id:
            return False
        new_email = data.get("new_email")
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        self.avatar_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()
        db.session.add(self)
        return True

    def generate_auth_token(self, expiration):
        """
        Generates an authentication token
        :param expiration: expiration time
        :return:
        """
        serializer = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
        return serializer.dumps({"id": self.id}).decode("ascii")

    def verify_auth_token(self, token):
        """
        Verifies the generated auth token
        :param token: token to verify
        :return: None or the user
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return self.query.get(data['id'])

    def can(self, permissions):
        """
        Checks if the current user has the given persmissions
        :param permissions:
        :return:
        """
        return self.role is not None and \
               (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        """
        Checks if the user is an admin
        :return: True if admin, False otherwise
        :rtype: bool
        """
        return self.can(Permission.ADMINISTER)

    def ping(self):
        """
        Pings the current user and updates their last seen attribute
        """
        self.last_seen = datetime.now()
        db.session.add(self)

    def __repr__(self):
        return "Id: {},\n uuid: {}, Username: {} ProfileId:{}, AccountStatusId:{}" \
               "Email:{} \n Dates: [created: {}, modified: {}]\n " \
               "Registered:{}\n Confirmed: [{} date: {}]\n Last Seen: {}" \
            .format(self.id, self.uuid, self.username, self.user_profile_id,
                    self.user_account_status_id, self.email, self.date_created,
                    self.date_modified, self.registered_on, self.confirmed,
                    self.date_modified, self.registered_on, self.confirmed,
                    self.confirmed_on, self.last_seen)

    def to_json(self):
        return dict(
            id=self.id, uuid=self.uuid, username=self.username,
            profile_id=self.user_profile_id, account_status_id=self.user_account_status_id,
            email=self.email, date_created=self.date_created,
            date_modified=self.date_modified, registered_on=self.registered_on,
            confirmed=self.confirmed, confirmed_on=self.confirmed_on,
            last_seen=self.last_seen, member_since=self.member_since
        )

    def from_json(self, user_account):
        user = json.loads(user_account)
        self.username = user["username"]
        self.email = user["email"]
        self.password_hash = user["password"]


# This callback is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return UserAccount.query.get(int(user_id))

"""
Models dealing with authentication

UserAccountStatus deals with the current account status details
UserAccount deals with authenticating the user, will handle login and authentication details
UserProfile is the actual user profile and will be used to display the user profile data
ExternalServiceAccount is for storing data for external service providers
"""
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from app.models import Base
from abc import ABCMeta
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declared_attr
from flask_login import UserMixin
from .. import db, login_manager
from datetime import datetime
from sqlalchemy.orm import relationship
import json


class UserAccountStatus(db.Model):
    """
    Stores the user's account status
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

    def __repr__(self):
        """
        Create human readable representation of user account status
        :return: string representation of user account status
        """
        return "Id: {}, Code:{}, Name:{}".format(self.id, self.code, self.name)


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
    last_seen = Column(DateTime)
    password_hash = Column(String(250), nullable=False)
    admin = Column(Boolean, nullable=True, default=False)
    registered_on = Column(DateTime, nullable=False)
    confirmed = Column(Boolean, nullable=False, default=False)
    confirmed_on = Column(DateTime, nullable=True)

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

    def __repr__(self):
        return "Id: {},\n uuid: {}, Username: {} ProfileId:{}, AccountStatusId:{}" \
               "Email:{} \n Dates: [created: {}, modified: {}]\n " \
               "Registered:{}\n Confirmed: [{} date: {}]\n Last Seen: {}" \
            .format(self.id, self.uuid, self.username, self.user_profile_id,
                    self.user_account_status_id, self.email, self.date_created,
                    self.date_modified,self.registered_on, self.confirmed,
                    self.confirmed_on, self.last_seen)

    def to_json(self):
        return dict(
            id=self.id, uuid=self.uuid, username=self.username,
            profile_id=self.user_profile_id,
            account_status_id=self.user_account_status_id,
            email=self.email, date_created=self.date_created,
            date_modified=self.date_modified, registerd_on=self.registered_on,
            confimed=self.confirmed, confirmed_on=self.confirmed_on,
            last_seen=self.last_seen
        )

    def from_json(self, user_account):
        user = json.loads(user_account)
        self.username = user["username"]
        self.email = user["email"]
        self.password_hash = user["password"]


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
    time_zone = Column(DateTime)

    def from_json(self, user_profile):
        user = json.loads(user_profile)
        self.first_name = user["first_name"]
        self.last_name = user["last_name"]
        self.email = user["email"]
        self.accept_tos = user["accept_tos"]
        self.time_zone = user["time_zone"]

    def to_json(self):
        return dict(
            first_name=self.first_name,
            last_name=self.last_name,
            date_created=self.date_created,
            date_modified=self.date_modified,
            email=self.email,
            accept_terms_of_service=self.accept_tos,
            time_zone=self.time_zone,
        )

    def __repr__(self):
        return "FirstName: {first_name}, LastName:{last_name}\n " \
               "Dates:[Created:{date_created}, Modified:{date_modified}]\n " \
               "Email:{email} accept_terms_of_service:{accept_tos}\n" \
               " TimeZone:{time_zone}".format(first_name=self.first_name,
                                              last_name=self.last_name,
                                              date_created=self.date_created,
                                              date_modified=self.date_modified,
                                              email=self.email,
                                              accept_tos=self.accept_tos,
                                              time_zone=self.time_zone, )


# This callback is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return UserAccount.query.get(int(user_id))


class ExternalServiceAccount(db.Model):
    """
    Abstract class that will superclass all external service accounts,

    :cvar first_name: first name as received from the external service account
    :cvar last_name: last name as received from external service account
    """
    __metaclass__ = ABCMeta
    __abstract__ = True

    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    @declared_attr
    def user_profile_id(self):
        """
        This is a declared attr, that will be used in all external accounts
        :return: User profile id that is a foreign and primary key
        """
        return Column(Integer, ForeignKey(UserProfile.id), primary_key=True)


class FacebookAccount(ExternalServiceAccount):
    """
    Facebook account details for the author
    :cvar __tablename__: name of this table as represented in the database
    :cvar facebook_id: Facebook id received from
    """
    __tablename__ = "facebook_account"
    facebook_id = Column(String(100), nullable=True, unique=True)

    def __init__(self, facebook_id, email, first_name, last_name):
        super().__init__(email, first_name, last_name)
        self.facebook_id = facebook_id


class TwitterAccount(ExternalServiceAccount):
    """
    Twitter account table
    :cvar __tablename__: table name as rep in database
    :cvar twitter_id: The twitter id as set in Twitter, or as received from Twitter
    """
    __tablename__ = "twitter_account"
    twitter_id = Column(String(100), nullable=True, unique=True)

    def __init__(self, twitter_id, email, first_name, last_name):
        super().__init__(email, first_name, last_name)
        self.twitter_id = twitter_id


class GoogleAccount(ExternalServiceAccount):
    """
    Google Account table
    :cvar __tablename__: name of table in database
    :cvar google_id: Google id as received from Google on registration
    """
    __tablename__ = "google_account"
    google_id = Column(String(100), nullable=True, unique=True)

    def __init__(self, google_id, email, first_name, last_name):
        super().__init__(email, first_name, last_name)
        self.google_id = google_id


class AsyncOperationStatus(Base):
    """
    Dictionary table that stores 3 available statuses, pending, ok, error
    """
    __tablename__ = "async_operation_status"

    code = Column("code", String(20), nullable=True)

    def __repr__(self):
        pass


class AsyncOperation(Base):
    """

    """
    __tablename__ = "async_operation"

    async_operation_status_id = Column(Integer, ForeignKey(AsyncOperationStatus.id))
    user_profile_id = Column(Integer, ForeignKey(UserProfile.id))

    status = relationship("AsyncOperationStatus", foreign_keys=async_operation_status_id)
    user_profile = relationship("UserProfile", foreign_keys=user_profile_id)

    def __repr__(self):
        pass

# todo add events
# event.listen(
#     AsyncOperationStatus.__table__, "after_create",
#     DDL(""" INSERT INTO async_operation_status (id,code) VALUES(1,'pending'),(2, 'ok'),(3, 'error'); """)
# )

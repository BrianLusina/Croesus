"""
Models dealing with authentication
"""
from sqlalchemy import Column, String, Integer, DateTime, func, ForeignKey, Boolean, Table
from app.models import Base
from hashlib import md5
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declared_attr
from flask_login import UserMixin
from .. import db, login_manager
from datetime import datetime
from sqlalchemy.orm import relationship, backref, dynamic


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


class UserAccount(Base):
    """
    User account model
    :cvar uuid unique user id
    :cvar first_name first name of user
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

    def __repr__(self):
        pass

    def to_json(self):
        pass

    def from_json(self):
        pass


class UserProfile(Base):
    """
    User profile. This will represent the actual information of the user
    :cvar first_name first name of user
    :cvar last_name user's last name
    :cvar email user's email address
    :cvar accept_terms_of_service boolean value indicating user accepts terms of service
    :cvar time_zone user's current timezone
    """
    __tablename__ = "user_profile"

    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    email = Column(String(250), nullable=False, unique=True, index=True)
    accept_terms_of_service = Column(Boolean, nullable=False, default=True)
    time_zone = Column(DateTime)

    def from_json(self):
        pass

    def __repr__(self):
        pass

    def to_json(self):
        pass


# This callback is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_author(user_id):
    return UserAccount.query.get(int(user_id))

# class Person(models.Model):
#     id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=1000, blank=True)
#     email = models.CharField(max_length=200)
#     title = models.CharField(max_length=100)
#     linkedin = models.CharField(max_length=200, null=True)
#     github = models.CharField(max_length=200, null=True)
#     twitter = models.CharField(max_length=200, null=True)
#     image = models.CharField(max_length=500)
#     responsibilities = models.CharField(max_length=1000, default='')
#     bio = models.CharField(max_length=1000, default='')
#     birthday = models.DateField(default=timezone.now)
#
#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.slug = slugify(self.first_name + self.last_name)
#         super(Person, self).save(*args, **kwargs)
#
#     def __repr__(self):
#         return "<id: %r, Title: %r, Name:<%r %r>, Email: %r ImgUrl: %r>" % (
#             self.id, self.title, self.first_name, self.last_name, self.email, self.image)
#
#     def __str__(self):
#         return self.first_name

from sqlalchemy import Column, String, Integer, DateTime, func, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship, backref, dynamic
from abc import ABCMeta, abstractmethod
from hashlib import md5
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declared_attr
from flask_login import UserMixin
from . import db, login_manager
from datetime import datetime


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

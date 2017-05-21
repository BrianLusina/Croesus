"""
Module for fetching blogs and news posts

This module will be used to fetch blog posts in the background and make them available as
an API to the client
"""

from flask import Blueprint

blog = Blueprint(name="blog", import_name=__name__, url_prefix="/blog/")

from . import views

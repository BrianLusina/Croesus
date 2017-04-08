from flask import Blueprint

home = Blueprint(name="home", url_prefix="/", import_name=__name__)

from . import views

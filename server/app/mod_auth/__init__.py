from flask import Blueprint

auth = Blueprint(name="auth", import_name=__name__, url_prefix="/auth/")

from . import views

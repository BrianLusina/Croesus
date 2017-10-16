from flask import Blueprint

auth = Blueprint(name="auth", import_name=__name__, url_prefix="/auth/",
                 template_folder="templates", static_folder="static")

from . import views

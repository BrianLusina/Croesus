from flask import Blueprint

home = Blueprint(name="home", url_prefix="/", import_name=__name__, template_folder="templates",
                 static_folder="static")

from . import views

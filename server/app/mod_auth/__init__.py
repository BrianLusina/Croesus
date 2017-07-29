from flask import Blueprint

<<<<<<< HEAD
auth = Blueprint(name="auth", import_name=__name__, url_prefix="/auth/")
=======
auth = Blueprint(name="auth", import_name=__name__, url_prefix="/auth/",
                 template_folder="templates", static_folder="static")
>>>>>>> remove log rocket dependency

from . import views

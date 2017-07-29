from flask import Blueprint

<<<<<<< HEAD
dashboard = Blueprint(name="dashboard", url_prefix="/dashboard/", import_name=__name__)
=======
dashboard = Blueprint(name="dashboard", url_prefix="/dashboard/", import_name=__name__,
                      template_folder="templates", static_folder="static")
>>>>>>> remove log rocket dependency

from . import views

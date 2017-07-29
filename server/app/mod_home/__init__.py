from flask import Blueprint

<<<<<<< HEAD
home = Blueprint(name="home", url_prefix="/", import_name=__name__, template_folder="templates",
                 static_folder="static")
=======
home = Blueprint(name="home", url_prefix="/", import_name=__name__)
>>>>>>> remove log rocket dependency

from . import views

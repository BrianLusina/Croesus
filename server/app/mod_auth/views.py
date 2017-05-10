from . import auth
from flask import jsonify


@auth.route("", methods=["GET", "POST"])
def login():
    pass

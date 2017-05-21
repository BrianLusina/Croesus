from . import auth
from flask import jsonify


@auth.route("login", methods=["GET", "POST"])
def login():
    pass


@auth.route("signup", methods=["GET", "POST"])
def signup():
    pass


@auth.route("reset", methods=["GET", "POST"])
def reset_password():
    pass

"""
Entry point to API application. This will be for running simple checks on the application

"""
from flask import jsonify, url_for, redirect, request
from flask_login import current_user
from . import home


@home.route("")
@home.route("home")
@home.route("index")
def index():
    """
    Entry point into the app
    :return: renders the home page
    """
    if current_user is not None:
        return redirect(url_for("dashboard.dashboard"))
    return jsonify({})

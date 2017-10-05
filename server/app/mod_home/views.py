"""
Entry point to API application. This will be for running simple checks on the application

"""
from flask import jsonify, url_for, redirect, request
from flask_login import current_user
from . import home
from ..__meta__ import __version__, __project__, __copyright__


@home.route("")
@home.route("home")
@home.route("index")
def index():
    """
    Entry point into the app
    :return: renders the api information
    """
    return jsonify({
        "version": __version__,
        "project": __project__,
        "copyright": __copyright__
    })

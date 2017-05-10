"""
Entry point to API application. This will be for running simple checks on the application

"""
from flask import render_template, jsonify
from . import home


@home.route("")
@home.route("home")
@home.route("index")
def index():
    """
    Entry point into the app
    :param request that will be handle by the url
    :return: renders the home page
    """
    return render_template("home.index.html")


@home.route("json", methods=["GET", "POST"])
def index_json():
    return jsonify(
        name="Brian", message="hello",
        list=["me", "them"]
    )

import newspaper
from flask import render_template, jsonify
from app.forms import ContactForm
from . import home
from app import celery


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


def contact(request):
    """
    Handles the contact form, picks data and sends the contact form to server
    :param request: the request handle by this function
    :return:
    """
    if request.method == "POST":
        form = ContactForm(request.POST)

    return None
from . import dashboard
from flask import render_template, url_for


@dashboard.route("")
def dashboard():
    return render_template("dashboard/dashboard.html")

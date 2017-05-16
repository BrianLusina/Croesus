from . import dashboard
from flask import render_template, url_for
from flask_login import login_required


@login_required
@dashboard.route("")
def dashboard():
    return render_template("dashboard.dashboard.html")

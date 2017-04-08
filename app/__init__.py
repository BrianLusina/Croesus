"""
This defines the application module that essentially creates a new flask app object
"""
from config import config
from flask import render_template, Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"


def create_app(config_name):
    """
    Creates a new flask app instance with the given configuration
    :param config_name: configuration to use when creating the application 
    :return: a new WSGI Flask app
    :rtype: Flask
    """
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # configure the application with the given configuration name, testing, development, production
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # initialize the db
    db.init_app(app)

    # initialize the login manager
    login_manager.init_app(app)

    error_handlers(app)
    register_app_blueprints(app)
    app_request_handlers(app)
    app_logger_handler(app)

    return app


def app_request_handlers(app):
    """
    This will handle all the requests sent to the application
    This will include before and after requests which could be used to update a user's status or the 
    database that is currently in use
    :param app: the current flask app
    """


def app_logger_handler(app):
    """
    Will handle error logging for the application and will store the app log files in a file that can 
    later be accessed.
    :param app: current flask application
    """


def error_handlers(app):
    """
    Error handlers function that will initialize error handling templates for the entire application
    :param app: the flask app
    """
    @app.errorhandler(404)
    def not_found(error):
        """
        This will handle errors that involve 404 messages
        :return: a template instructing user they have sent a request that does not exist on the server
        """


def register_app_blueprints(app):
    """
    Registers the application blueprints
    :param app: the current flask app
    """
    from app.mod_dashboard import dashboard
    from app.mod_home import home

    app.register_blueprint(home)
    app.register_blueprint(dashboard)

# coding=utf-8
"""
This defines the application module that essentially creates a new flask app object
"""
import os
from datetime import datetime

import jinja2
import redis
from celery import Celery
from flask import Flask, g
from flask_login import LoginManager, current_user
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import logging

from config import config, Config

# initialize objects of flask extensions that will be used and then initialize the application
# once the flask object has been created and initialized. 1 caveat for this is that when
#  configuring Celery, the broker will remain constant for all configurations
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
celery = Celery(__name__, broker=os.environ.get("CELERY_BROKER_URL"),
                backend=os.environ.get("CELERY_RESULT_BACKEND"))

# redis_db = redis.StrictRedis(host=os.environ.get("REDIS_SERVER"),
#                              port=os.environ.get("REDIS_PORT"), db=os.environ.get("REDIS_DB"))
logger = logging.getLogger("Croesus-Server")


class CroesusApp(Flask):
    """
    Custom application class subclassing Flask application. This is to ensure more modularity in
     terms of static files and templates. This way a module will have its own templates and the
      root template folder will be more modularized and easier to manage
    """

    def __init__(self):
        """
        jinja_loader object (a FileSystemLoader pointing to the global templates folder) is
        being replaced with a ChoiceLoader object that will first search the normal
        FileSystemLoader and then check a PrefixLoader that we create
        """
        Flask.__init__(self, __name__, static_folder="static", template_folder="templates")
        self.jinja_loader = jinja2.ChoiceLoader([
            self.jinja_loader,
            jinja2.PrefixLoader({}, delimiter=".")
        ])

    def create_global_jinja_loader(self):
        """
        Overriding to return the loader set up in __init__
        :return: jinja_loader 
        """
        return self.jinja_loader

    def register_blueprint(self, blueprint, **options):
        """
        Overriding to add the blueprints names to the prefix loader's mapping
        :param blueprint: 
        :param options: 
        """
        Flask.register_blueprint(self, blueprint, **options)
        self.jinja_loader.loaders[1].mapping[blueprint.name] = blueprint.jinja_loader


def create_app(config_name):
    """
    Creates a new flask app instance with the given configuration
    :param config_name: configuration to use when creating the application 
    :return: a new WSGI Flask app
    :rtype: Flask
    """
    app = CroesusApp()

    # configure the application with the given configuration name, testing, development,
    # production

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # configure celery
    celery.conf.update(app.config)

    # initialize the db
    db.init_app(app)

    # redis_db.set(name="host", value=os.environ.get("REDIS_SERVER"))
    # redis_db.set(name="port", value=os.environ.get("REDIS_PORT"))
    # redis_db.set(name="db", value=os.environ.get("REDIS_DB"))

    # initialize the login manager
    login_manager.init_app(app)

    # initialize flask mail
    mail.init_app(app)

    error_handlers(app)
    register_app_blueprints(app)
    app_request_handlers(app, db)
    app_logger_handler(app, config_name)
    app_request_handlers(app, db)
    app_logger_handler(app, config_name)

    register_app_blueprints(app)

    # this will reduce the load time for templates and increase the application performance
    app.jinja_env.cache = {}

    return app


def app_request_handlers(app, db_):
    """
    This will handle all the requests sent to the application
    This will include before and after requests which could be used to update a user's status or
     the database that is currently in use
    :param app: the current flask app
    """

    @app.before_request
    def before_request():
        """
        Before submitting the request, change the currently logged in user 'last seen' status to now
        this will update the database last_seen column and every time the user makes a request (refreshes the
        page), the last seen will be updated. this is called before any request is ma
        """
        g.user = current_user
        if current_user.is_authenticated:
            current_user.last_seen = datetime.now()
            db.session.add(g.user)
            db_.session.add(current_user)
            db_.session.commit()

            # @app.after_request
            # def after_request(response):
            #     for query in get_debug_queries():
            #         if query.duration >= DATABASE_QUERY_TIMEOUT:
            #             app.logger.warning(
            #                 "SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" %
            #                 (query.statement, query.parameters, query.duration,
            #                  query.context))
            #     return response


def app_logger_handler(app, config_name):
    """
    Will handle error logging for the application and will store the app log files in a file
    that can later be accessed.
    :param app: current flask application
    """
    import logging
    from logging.handlers import SMTPHandler, RotatingFileHandler
    MAIL_SERVER = app.config.get("MAIL_SERVER")

    if app.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if config_name == "production":
        if not app.debug and MAIL_SERVER != "":
            credentials = None

            MAIL_USERNAME = app.config.get("MAIL_USERNAME")
            MAIL_PASSWORD = app.config.get("MAIL_PASSWORD")

            if MAIL_USERNAME or MAIL_PASSWORD:
                credentials = (MAIL_USERNAME, MAIL_PASSWORD)

            mail_handler = SMTPHandler(mailhost=(MAIL_SERVER, app.config.get("MAIL_HOST")),
                                       fromaddr="no-reply@" + MAIL_SERVER,
                                       toaddrs=app.config.get("ADMINS"),
                                       subject="Arco app failure",
                                       credentials=credentials)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        if not app.debug and os.environ.get("HEROKU") is None:
            # log file will be saved in the tmp directory
            file_handler = RotatingFileHandler(filename="tmp/arco.log", mode="a", maxBytes=1 * 1024 * 1024,
                                               backupCount=10)
            file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%('
                                                        'lineno)d]'))
            app.logger.setLevel(logging.INFO)
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
            app.logger.info("Arco Blog")


def error_handlers(app):
    """
    Error handlers function that will initialize error handling templates for the entire application
    :param app: the flask app
    """

    @app.errorhandler(404)
    def not_found(error):
        """
        This will handle errors that involve 404 messages
        :return: a template instructing user they have sent a request that does not exist on
         the server
        """


def register_app_blueprints(app_):
    """
    Registers the application blueprints
    :param app: the current flask app
        return error, 404
        """
    from app.mod_dashboard import dashboard
    from app.mod_home import home
    from app.mod_blog import blog
    from app.mod_auth import auth
    app_.register_blueprint(auth)
    app_.register_blueprint(home)
    app_.register_blueprint(dashboard)
    app_.register_blueprint(blog)

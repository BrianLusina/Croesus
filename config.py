"""
Configurations for flask application. These are global variables that the app will use in its entire
lifetime
"""
import os
from abc import ABCMeta, abstractmethod

basedir = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    """
    Default configuration for application
    This is abstract and thus will not be used when configuring the application. the instance variables
    and class variables will be inherited by subclass configurations and either they will be used as is
    of there will be overrides
    :cvar THREADS_PER_PAGE: Application threads. A common general assumption is
    using 2 per available processor cores - to handle
    incoming requests using one and performing background
    operations using the other.
    :cvar CSRF_SESSION_KEY Use a secure, unique and absolutely secret key for signing the data.
    :cvar SQLALCHEMY_DATABASE_URI Define the database - we are working with SQLite for this example    
    """

    __abstract__ = True
    __metaclass__ = ABCMeta

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'arco'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT") or 'precious_arco'
    ROOT_DIR = APP_ROOT
    WTF_CSRF_ENABLED = True
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY")
    THREADS_PER_PAGE = 2
    DATABASE_CONNECT_OPTIONS = {}

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    # MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    # MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']
    #
    # MAIL_DEFAULT_SENDER = os.environ["MAIL_DEFAULT_SENDER"]
    #
    # # credentials for external service accounts
    # OAUTH_CREDENTIALS = {
    #     "facebook": {
    #         "id": os.environ["FACEBOOK_ID"],
    #         "secret": os.environ["FACEBOOK_SECRET"]
    #     },
    #     "google": {
    #         "id": os.environ["GOOGLE_ID"],
    #         "secret": os.environ["GOOGLE_SECRET"]
    #     }
    # }

    @staticmethod
    def init_app(app):
        """Initializes the current application"""
        pass


class DevelopmentConfig(Config):
    """Configuration for development environment"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(Config):
    """
    Testing configurations
    """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    """
    Production configuration
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    ADMINS = [os.environ.get("ADMIN_EMAIL_1")]


config = {
    'develop': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

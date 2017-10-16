import os
import better_exceptions
from flask_migrate import Migrate, MigrateCommand, upgrade
from flask_script import Manager, Shell, Server
from app import create_app, db, app_logger
import alembic
import alembic.config
from sqlalchemy.exc import IntegrityError

# create the application with given configuration from environment
app = create_app(os.getenv("FLASK_CONFIG") or "default")
port = 5000

# import the data with app context
# this prevents the data from being deleted after every migration
# with app.app_context():
#     from app.models import *

manager = Manager(app)
migrate = Migrate(app, db, directory="migrations")
server = Server(host="127.0.0.1", port=port)
public_server = Server(host="0.0.0.0", port=port)


def make_shell_context():
    """
    Makes a shell context
    :return dictionary object
    :rtype: dict
    """
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)
manager.add_command("runserver", server)
manager.add_command("publicserver", public_server)


@manager.command
def test(cover=False):
    """Run the unit tests."""
    import coverage
    cov = coverage.coverage(branch=True, include='app/*')
    cov.start()

    if cover and not os.environ.get('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if cover:
        cov.stop()
        cov.save()
        print("Coverage Summary:")

        cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'coverage')

        # generate html report
        cov.html_report(directory=covdir)

        # generate xml report
        cov.xml_report()

        print("HTML version: file://{}/index.html".format(covdir))
        print("XML version: file://{}".format(basedir))
        cov.erase()


@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import upgrade

    # migrate database to latest revision
    upgrade()


@manager.command
def profile(length=25, profile_dir=None):
    """
    This module provides a simple WSGI profiler middleware for finding 
    bottlenecks in web application. It uses the profile or cProfile 
    module to do the profiling and writes the stats to the stream provided
    
    see: http://werkzeug.pocoo.org/docs/0.9/contrib/profiler/
    """
    from werkzeug.contrib.profiler import ProfilerMiddleware

    app.config["PROFILE"] = True
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length], profile_dir=profile_dir)
    app.run()


@manager.option('-m', '--migration', help='create database from migrations',
                action='store_true', default=None)
def init_db(migration):
    """drop all databases, instantiate schemas"""
    db.drop_all()

    if migration:
        # create database using migrations
        print("applying migrations")
        upgrade()
    else:
        # create database from model schema directly
        db.create_all()
        db.session.commit()
        cfg = alembic.config.Config("app/migrations/alembic.ini")
        alembic.command.stamp(cfg, "head")


@manager.option('-e', '--email', help='email address', required=True)
@manager.option('-p', '--password', help='password', required=True)
@manager.option('-a', '--admin', help='make user an admin user', action='store_true', default=None)
def user_add(email, password, admin=False):
    from app.mod_auth.models import UserAccount
    """add a user to the database"""
    user_account = UserAccount.query.filter_by(email=email).first()
    if user_account:
        app_logger.error("User with email {} already exists".format(email))
    else:
        user = UserAccount(email=email, password=password, username=email)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            app_logger.exception("Failed to save user with email :{}".format(email))


@manager.option('-e', '--email', help='email address', required=True)
def user_del(email):
    """delete a user from the database"""
    from app.mod_auth.models import UserAccount
    user_account = UserAccount.query.filter_by(email=email)
    if user_account:
        db.session.delete(user_account)
        app_logger.info("User with email: {} deleted".format(email))
    else:
        app_logger.error("User with email: {} does not exist in DB".format(email))



@manager.command
def drop_db():
    """drop all databases, instantiate schemas"""
    db.reflect()
    db.drop_all()


if __name__ == "__main__":
    try:
        app_logger.info("Running on address {}:{}".format(server.host, server.port))
    except Exception:
        app_logger.info("Running on address {}:{}".format(public_server.host, public_server.port))
    manager.run()

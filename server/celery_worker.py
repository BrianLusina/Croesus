"""
Celery worker script

This process needs to have its own Flask application instance that can be used to create 
the context necessary for the Flask background tasks to run. 

This creates a Flask application and pushes an application context, which will remain set
 through the entire life of the process.

:usage:
(venv) $ celery worker -A celery_worker.celery --loglevel=info 
"""
import os

# celery import is necessary, even though it will not be used here. it is vital for celery
# to run
from app import create_app, celery
from setup_environment import setup_environment_variables
import click

# import environment variables
setup_environment_variables()

# log info
click.echo(click.style("Running celery worker", fg="yellow", bg="black", bold=True))

app = create_app(os.environ.get("FLASK_CONFIG", "default"))
app.app_context().push()

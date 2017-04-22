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

from web.app import create_app
from setup_environment import setup_environment_variables

# import environment variables
setup_environment_variables()

app = create_app(os.environ.get("FLASK_CONFIG", "default"))
app.app_context().push()

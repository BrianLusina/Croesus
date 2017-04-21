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
from app import celery, create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")
app.app_context().push()

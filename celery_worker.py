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

# import environment variables
if os.path.exists(".env"):
    print("Importing environment variables")
    for line in open(".env"):
        var = line.strip().split("=")
        if len(var) == 2:
            os.environ[var[0]] = var[1]

app = create_app(os.environ.get("FLASK_CONFIG", "default"))
app.app_context().push()

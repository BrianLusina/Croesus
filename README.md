# Arco Project


## Project Structure

    arco/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    teamdirectory/
        migrations/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
    userdashboard/
        migrations/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py        
    www/
        migrations/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py    
    .gitignore
    LICENSE
    manage.py
    README.md
    requirements.txt

## Project Files

1. __manage.py__
    Command line utility that lets you interact with Django project TreasureGram

2. __<app>/__init__.py__
    Empty file that tells Python that this directory should be considered a Python package
    
3. __<app>/settings.py__
    Settings for this Django Project

4. __<app>/urls.py__
    URL declarations for this Django project. A table of contents for Django powered site

5. __<app>/wsgi.py__
   Entry point for WSGI compatible web servers to save your project
  
    
### teamdirectory app
  
  An app displaying the team involved in building this application
  
## Models

This defines the data structure and communicates with the database. It is a good way to organize the data.
Create your tables here that will define your tables to be mapped with Django's ORM to an SQL database.


## The admin

The admin site allows you to perform administrative tasks. These tasks can be performed by authorized users only. To do this you will need to create superusers with this command:

``` bash
python manage.py createsuperuser
```

You will then have to enter a username, email and password

After which you can go to `localhost:8000/admin` and log in using your credentials.

After logging in you will not be able to see your models, this is because you have to register them first. The registration is done using `admin.py`

## URL Dispatcher Best Practices

### Refactoring the project's URLs dispatcher
First remove the index/ from the regex and match an empty path to load the view

``` python
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main_app.urls'))
]
```
> This will still perform the same function as before when the url(r'^index/', views.index)
 
## The App URLs Dispatcher

It is best practice to have a project URL dispatcher and an app URL dispatcher. The Projects URL dispatcher is handling all the requests but it is best practice to funnel all the app specific requests to an **App's URL dispatcher**
Thus in the project's url dispatcher we need to include the app's url dispatcher

### Creating the App's url dispatcher

First import `url` from `django.conf.urls` then import the views

``` python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^$', view=views.index)
]
```

## URL-View Template Process

The client will request for a specific url, the URL dispatcher will match this to a correct view and the *View* will collect needed data and render the *Template*. The Template simply defines the URL to be rendered.

You will need to create a templates directory in every app that you will have in your project.
First register your app in the projects `settings` file.

In the `settings.py` file, you will find a list called `INSTALLED_APPS`, register your application name there.
Then render the template in the views like so:
    
    
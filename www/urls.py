from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'', view=views.home, name="home"),
    url(regex=r'/about', view=views.home, name="about"),
    url(regex=r'/contact', view=views.home, name="contact"),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^team$', view=views.team_directory)
]

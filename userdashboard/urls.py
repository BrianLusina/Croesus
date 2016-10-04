from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'user/', view=views.dashboard, name="dashboard"),
]

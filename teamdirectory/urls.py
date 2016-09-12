from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^team$', view=views.team_directory),
    url(regex=r"^members/([a-z0-9-]+)", view=views.member_detail, name="member_detail"),
]

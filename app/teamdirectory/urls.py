from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'', view=views.team_directory, name="team_directory"),
    url(regex=r'members/([a-z0-9-]+)/$', view=views.member_detail, name="member_detail"),
    url(regex=r'members/([a-z0-9-]+)/edit/$', view=views.member_edit, name='edit'),
]
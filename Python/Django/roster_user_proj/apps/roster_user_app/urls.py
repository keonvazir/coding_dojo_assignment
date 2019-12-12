from django.conf.urls import url
from . import views

urlpattenrs = [
    url(r'^$', views.index),
    url(r'^users$', views.users_page),
    url(r'^users/add_user$', views.add_user),
    url(r'^rosters/add_roster', views.add_roster),
    url(r'^rosters/(?P<roster_id>\d+)$', views.one_roster),
    url(r'^users/(?P<user_id>\d+)$', views.one_user),

]
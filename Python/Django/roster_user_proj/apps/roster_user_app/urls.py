from django.conf.urls import url
from . import views

urlpattenrs = [
    url(r'^$', views.index),
    url(r'^users$', views.users_page),
    url(r'^users/add_user$', views.add_user),
    url(r'^rosters/add_roster', views.add_roster),
    url(r'^rosters/(?P<roster_id>\d+)$', views.one_roster),
    url(r'^users/(?P<user_id>\d+)$', views.one_user),
    url(r'^users/(?P<user_id>\d+)/add_roster$', views.add_roster_to_user),
    url(r'^rosters/(?P<roster_id>\d+)/add_user$', views.add_user_to_roster),

]
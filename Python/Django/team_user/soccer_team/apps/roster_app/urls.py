from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^players$', views.players_page),
    url(r'^players/add_player', views.add_player),
    url(r'^rosters/add_roster', views.add_roster),
    url(r'players/(?P<player_id>\d+)$', views.one_player),
    url(r'rosters/(?P<roster_id>\d+)$', views.one_roster),
    url(r'rosters/(?P<roster_id>\d+)/add_player$', views.add_player_to_roster),
    url(r'players/(?P<player_id>\d+)/add_roster$', views.add_roster_to_player),


]
######## APP LEVEL urls.py #############

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.root),
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.add_new_show),
    url(r'^shows/(?P<id>\d+)$', views.new_show),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit),
    url(r'^create$', views.create),
]
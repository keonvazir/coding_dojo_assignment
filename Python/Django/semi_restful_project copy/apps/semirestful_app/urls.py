######## APP LEVEL urls.py #############

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    # url(r'^$', views.root),
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.add_new_show),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<restful_id>\d+)$', views.one_show),
    url(r'^shows/(?P<restful_id>\d+)/edit$', views.edit_page),
    url(r'^shows/(?P<restful_id>\d+)/update$', views.update),
    url(r'^shows/(?P<restful_id>\d+)/destroy$', views.delete),
]
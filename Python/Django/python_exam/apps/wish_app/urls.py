####### APP LEVEL #########

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^wishes$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^new$', views.reg),
    url(r'^wishes/edit/(?P<wish_id>\d+)$', views.edit_page),
    url(r'^wishes/new$', views.new_wish),
    url(r'wishes/add_wish$', views.add_wish),
    url(r'^wishes/edit_wish/(?P<wish_id>\d+)$', views.edit_wish),
    url(r'^wishes/(?P<wish_id>\d+)/destroy$', views.remove),
    url(r'^wishes/(?P<wish_id>\d+)/granted$', views.granted),
    url(r'^wishes/(?P<wish_id>\d+)/like$', views.like)
]
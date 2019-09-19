########## APP LEVEL urls.py ###########

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.root),
    url(r'^index$', views.index),
    url(r'^success$', views.success),
    url(r'^reg$', views.reg),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]

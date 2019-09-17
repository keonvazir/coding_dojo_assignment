########### APP LEVEL urls.py file #############

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
]
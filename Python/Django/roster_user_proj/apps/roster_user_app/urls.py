from django.conf.urls import url
from . import views

urlpattenrs = [
    url(r'^$', views.index),

]
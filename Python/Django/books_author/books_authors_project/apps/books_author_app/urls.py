############ APP LEVEL urls.py ##############

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.authors_page),
    url(r'^authors/add_author$', views.add_author),
    url(r'^books/add_book$', views.add_book),
    url(r'^books/(?P<book_id>\d+)/add_author$', views.add_author_to_book),
    url(r'^books/(?P<book_id>\d+)$', views.one_book),
    url(r'^authors/(?P<author_id>\d+)$', views.one_author),
    url(r'^authors/(?P<author_id>\d+)/add_book$',views.add_book_to_author),
]
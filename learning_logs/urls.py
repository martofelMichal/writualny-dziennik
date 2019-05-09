"""Definiuje wzorce adresow URL dla learning_logs"""

from django.conf.urls import url
from . import views

urlpatterns = [
    #strona główna
    url(r'^$', views.index, name='index'),

    #wyswietlenie wszystkich tematow
    url(r'^topics/$', views.topics, name='topics'),

    #strona szczegolowa dotyczaca pojedynczego tematu
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #strona przeznaczona do dodawnia nowego tematu
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #strona przeznaczona do dodawania nowego wpisu
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #strona przeznaczona do edycji wpisu
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

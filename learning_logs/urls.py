"""Defines URL patters for learning_logs."""

from django.conf.urls import url
from . import views

urlpatterns = [
    #Home Page
    url(r'^$', views.index, name='index'),
    # In the first argument, r tells python to interpret the following string as
    # a raw string and the quotes tell python where the regular expresss begins and ends
    # the ^ tells python to find the beginning of the string and the $ tells python to
    # look for the end of the string

    # Show all topics.
    url(r'^topics/$', views.topics, name='topics'),
    #detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]

"""Defines URL patters for learning_logs."""

from django.conf.urls import urls
from . import views

urlpatterns = [
    #Home Page
    url(r'^$', views.index, name='index'),
    # In the first argument, r tells python to interpret the following string as
    # a raw string and the quotes tell python where the regular expresss begins and ends
    # the ^ tells python to find the beginning of the string and the $ tells python to 
    # look for the end of the string
]

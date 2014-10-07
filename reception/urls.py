from django.conf.urls import patterns, url
from reception import views

urlpatterns = patterns('',
                       url(r'^$', views.index),
                       )

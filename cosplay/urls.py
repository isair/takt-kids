from django.conf.urls import patterns, url
from cosplay import views

urlpatterns = patterns('',
                       url(r'^$', views.login),
                       url(r'^dashboard/$', views.dashboard),
                       url(r'^vote/jury/$', views.juryvote),
                       url(r'^top/$', views.top_cosplayers),
                       )

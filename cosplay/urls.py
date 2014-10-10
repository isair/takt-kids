from django.conf.urls import patterns, url
from cosplay import views

urlpatterns = patterns('',
                       url(r'^$', views.login),
                       url(r'^wait/$', views.wait),
                       url(r'^dashboard/$', views.dashboard),
                       )

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'takt_kids.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^report_builder/', include(
                           'report_builder.urls')),
                       url(r'', include('social_auth.urls')),
                       url(r'^', include(admin.site.urls)),
                       )

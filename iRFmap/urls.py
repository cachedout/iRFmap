from django.conf.urls import patterns, include, url
from tastypie.api import Api
from iRFmap.api import *

v1_api = Api(api_name='v1')
v1_api.register(RunnerResource())
v1_api.register(RaceResource())




# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'iRFmap.views.home', name='home'),
                       # url(r'^iRFmap/', include('iRFmap.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^map/', 'iRFmap.views.map_view', name='map'),
                       url(r'^api/', include(v1_api.urls)),
                       url(r'^poll_leaderboard/(?P<race_id>\d+)', 'iRFmap.views.poll_leaderboard',
                           name='poll_leaderboard'),

)

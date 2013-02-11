from django.conf.urls import patterns, include, url
from django.contrib import admin

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
    url(r'^map/', 'iRFmap.views.map', name='map'),
    url(r'^poll_leaderboard/(?P<race_id>\d+)', 'iRFmap.views.poll_leaderboard', name='poll_leaderboard'),
)

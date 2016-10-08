
from django.conf.urls import include, url
from django.contrib import admin
from .views import *
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^(?P<type>\w+)/(?P<id>\d+)/(?P<status>\d+)', device),
	#url(r'^led/(?P<led_id>\d+)/(?P<status>\d+)/$', led ),
	#url(r'^fan/(?P<fan_id>\d+)/(?P<status>\d+)/$', fan ),
	url(r'^buzzer/$' , buzzer ),
	url(r'^temp/$', temp ),
	url(r'^status/$', status),
	url(r'^allon/$', allon),
	url(r'^alloff/$', alloff),
	url(r'^lock/$', lockdown),
]


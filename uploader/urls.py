
#
#	author: Neil Barry-Murphy
# 	Modified by David Kelly to work for saving competition submissions
#

from django.conf.urls import patterns, url
from django.contrib import admin
from uploader import views

admin.autodiscover()

urlpatterns = patterns('uploader.views',
	url(r'^$', views.home, name='upload'),
	url(r'^upload_complete/$', views.upload_complete, name='upload_complete'),
)

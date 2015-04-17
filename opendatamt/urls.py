
#
#	author: Neil Barry-Murphy
#
#	Modified by David Kelly 03-04-2015
#	Moved all accounts urls to a separate django app 
#

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()
from accounts import views

urlpatterns = patterns('',
	# Show login on homepage
	url(r'^$', views.login),
	# admin url
	url(r'^admin/', include(admin.site.urls)),
	#general app inclusions
	url(r'^comp_entries/', include('comp_entries.urls', namespace="comp_entries")),
    url(r'^uploader/', include('uploader.urls', namespace="uploader")),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^teams/', include('teams.urls', namespace="teams")),
	url(r'^accounts/', include('accounts.urls', namespace="accounts")),
)	+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
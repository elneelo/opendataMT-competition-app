
#
#	author: David Clince & Neil Barry-Murphy
#

from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('comp_entries.views',
	url(r'^$', 'entries_home', name='entries_home'),
	url(r'^(?P<comp_id>\d+)/$', 'entries_detail', name='entries_detail'),
	url(r'^search/$', 'search_titles', name='search_titles'),
)
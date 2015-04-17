from django.conf.urls import patterns, url
from teams import views

urlpatterns = patterns('',
	url(r'^$', views.all_teams, name='all_teams'),
	url(r'^(?P<team_id>\d+)/$', views.team_info, name='team_info'),
)
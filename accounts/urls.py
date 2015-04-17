from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
	#user authentication urls
	url(r'^login/$', views.login, name='login'),
	url(r'^alt_login/$', views.alt_login, name='alt_login'),
	url(r'^auth/$', views.auth_view, name='auth_view'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^loggedin/$', views.loggedin, name='loggedin'),
	url(r'^invalid/$', views.invalid_login, name='invalid_login'),
	url(r'^not_a_team_member/$', views.need_team_membership, name='need_team_membership'),
	#registering users
	url(r'^register/$', views.register_user, name='register_user'),
	url(r'^register_success/$', views.register_success, name='register_success'),
)
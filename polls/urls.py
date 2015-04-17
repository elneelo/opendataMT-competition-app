
#
#	author: Neil Barry-Murphy
#

from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('polls.views',
    # ex: /polls/
    url(r'^$', 'polls_home', name='polls_home'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', 'detail', name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', 'results', name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', 'vote', name='vote'),
)

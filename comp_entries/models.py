
#
#	author: David Clince & Neil Barry-Murphy
#

from django.db import models
from datetime import datetime, timedelta
from django.contrib import admin
from teams.models import Team
from django.utils import timezone
	
class CompetitionManager(models.Manager):
	# Returns all active competitions
	def are_active(self):
		result = Competition.objects.all()
		for comp in result:
			if comp.still_active() is False: comp.delete()
		return result

	# Returns all active competitions for the given team
	def active_team_comps(self, team):
		result = Competition.objects.filter(teams=team)
		for comp in result:
			if comp.still_active() is False: comp.delete()
		return result

class Competition(models.Model):
	objects = CompetitionManager()
	teams = models.ManyToManyField(Team)
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=2000)
	deadline_date = models.DateTimeField('deadline date')
	creation_date = models.DateTimeField('creation date')
	
	def __str__(self):
		return self.name
	
	def still_active(self):
		return timezone.now() <= self.deadline_date
	still_active.admin_order_field = 'creation_date'
	still_active.boolean = True
	still_active.short_description = 'Active?'

	def get_deadline_date():
		return datetime.today() + timedelta(days=30)
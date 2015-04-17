from django.db import models
from django.contrib.auth.models import User
from teams.models import Team

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	team = models.ForeignKey(Team)

	def __str__(self):
		return self.user.username
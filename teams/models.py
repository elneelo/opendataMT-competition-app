from django.db import models

class Team(models.Model):
	name = models.CharField(max_length=50)
	university = models.CharField(max_length=300, blank=True)
	
	def __unicode__(self):
		return self.name
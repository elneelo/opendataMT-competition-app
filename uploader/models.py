
#
#	author: Neil Barry-Murphy
#	Modified by David Kelly to work for saving competition submissions
#

from django.db import models
from django.contrib.auth.models import User
from comp_entries.models import Competition
from teams.models import Team

class Upload(models.Model):
    submission = models.FileField("Submission File", upload_to="uploaded_files/")    
    upload_date = models.DateTimeField('upload date')
    user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    competition = models.ForeignKey(Competition)
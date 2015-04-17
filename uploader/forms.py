
#
#	author: Neil Barry-Murphy
#	Modified by David Kelly to work for saving competition submissions
#

from django.forms import ModelForm
from models import Upload

from comp_entries.models import Competition

# FileUpload form class.
class UploadForm(ModelForm):

    class Meta:
        model = Upload
        fields = ('competition', 'submission',)

    def __init__(self, user, *args, **kwargs):
    	super(UploadForm, self).__init__(*args, **kwargs)
        team = user.userprofile.team
        # only show active competitions
        self.competition = Competition.objects.active_team_comps(team)
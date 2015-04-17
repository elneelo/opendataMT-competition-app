from django.shortcuts import render, get_object_or_404
from models import Team

# Create your views here.
def all_teams(request):
	teams = Team.objects.all()
	context = {'teams':teams}
	return render(request, 'teams/all_teams.html', context)

def team_info(request, team_id):
	team = get_object_or_404(Team, id=team_id)
	context = {'team':team}
	return render(request, 'teams/team_info.html', context)
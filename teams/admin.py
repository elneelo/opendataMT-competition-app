from django.contrib import admin
from accounts.admin import UserProfileTeamInline
from models import Team

class TeamAdmin(admin.ModelAdmin):
	fieldsets = [
		('Team Information', {'fields':['name', 'university']}),
	]

	list_display = ('name', 'university',)
	search_fields = ['name']
	inlines = [UserProfileTeamInline]


admin.site.register(Team, TeamAdmin)

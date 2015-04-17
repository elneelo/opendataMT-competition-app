
#
#	author: David Clince & Neil Barry-Murphy
#
from django.contrib import admin
from comp_entries.models import Competition

class CompAdmin(admin.ModelAdmin):
	fieldsets = [
		('Competition Information', {'fields':['name', 'description']}),
		('Date Information', {'fields':['creation_date','deadline_date']}),
		('Participating Teams', {'fields':['teams']})
	]
	list_display = ('name', 'creation_date', 'deadline_date', 'still_active')
	list_filter = ['creation_date']
	search_fields = ['name']

admin.site.register(Competition, CompAdmin)
#admin.site.register(Submission, SubAdmin)



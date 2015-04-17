
#
#	author: Neil Barry-Murphy
#	Modified by: David Kelly
#

from django.contrib import admin
from uploader.models import Upload

class UploadAdmin(admin.ModelAdmin):
	readonly_fields = ('upload_date', 'user', 'team', 'competition', )
	fieldsets = [
		('File Information', {'fields':['submission', 'upload_date']}),
		('Team Information', {'fields':['user', 'team']}),
		('Competition Information', {'fields':['competition']})
	]
	list_display = ('upload_date', 'team', 'competition',)
	search_fields = ['competition']

admin.site.register(Upload, UploadAdmin)
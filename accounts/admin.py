from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import UserProfile

class UserProfileInline(admin.StackedInline):
	model = UserProfile

class UserProfileTeamInline(admin.StackedInline):
	model = UserProfile
	extra = 3

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

#this is for the home page
def login(request):
	return render(request, 'accounts/login.html')

#this is used to gain access to apps ... (eg. uploader)
def alt_login(request):
	return render(request, 'accounts/alt_login.html')

#work needs to be done to this method with regards to contextrequests.
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
	return render(request, 'accounts/loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
	return render(request, 'accounts/invalid_login.html')


def logout(request):
	auth.logout(request)
	return render(request, 'accounts/logout.html')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')
	else:
		context = {'form':UserCreationForm()}
		return render(request, 'accounts/register.html', context)

def register_success(request):
	return render(request, 'accounts/register_success.html')

def need_team_membership(request):
	return render(request, 'accounts/need_team_membership.html')
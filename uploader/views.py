
#
#   author: Neil Barry-Murphy
#   Modified by David Kelly to work for saving competition submissions
#

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from uploader.forms import UploadForm
from django.utils import timezone

@login_required(login_url='/accounts/alt_login/')
def home(request):
    if hasattr(request.user, 'userprofile'):
        form = UploadForm(request.user)
        if request.method=="POST":
            form = UploadForm(request.user, request.POST, request.FILES)       
            if form.is_valid():
                # save the upload
                upload = form.save(commit = False)
                upload.upload_date = timezone.now()
                upload.user = request.user
                upload.team = request.user.userprofile.team
                upload.save()
                return HttpResponseRedirect(reverse('uploader:upload_complete'))
        return render(request,'uploader/home.html',{'form':form})
    else: 
        return HttpResponseRedirect(reverse('accounts:need_team_membership'))

def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    return response

def upload_complete(request):
	return render(request, "uploader/upload_complete.html")
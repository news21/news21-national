# -*- coding: utf-8 -*-
from django.contrib.auth.forms import *
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import datetime
from django_authopenid.forms import *
from django_authopenid.models import UserAssociation
from django.core.files.base import ContentFile

from news21national.core.forms import ProfileForm
from news21national.core.models import Profile
from news21ams.editorsdesk.models import EditorsDesk
from news21ams.newsroom.models import Newsroom
from news21ams.partner.models import Partner, PartnerForm
from news21ams.story.models import MetaStory
from news21ams.multimedia.models import Media

def home(request):
	form1 = OpenidSigninForm()
	form2 = AuthenticationForm()
	return render_to_response("core/home.html", {'form1': form1,'form2': form2}, context_instance=RequestContext(request))

def privacy(request):
   return render_to_response("core/privacy.html", {}, context_instance=RequestContext(request))

def terms(request):
   return render_to_response("core/terms.html", {}, context_instance=RequestContext(request))

@login_required
def dashboard(request):
	# first if the user is an editor if so send them to editor's desk
	if request.user.is_staff:
		return HttpResponseRedirect(reverse('editorsdesk_dashboard'))
	
	# check to see if user is associated with newsroom or partner ... if neither ... send to association page
	n_count = Newsroom.objects.filter(members=request.user).distinct().count()
	p_count = Partner.objects.filter(members=request.user).distinct().count()
	e_count = EditorsDesk.objects.filter(editors=request.user).distinct().count()
	if n_count == 0 and p_count == 0 and e_count == 0:
		return HttpResponseRedirect(reverse('user_association'))

	# if user is part of a partner ... send to seperate dashboard
	if p_count > 0:
		return HttpResponseRedirect(reverse('partner_dashboard'))

	# if user is an editor ... send to seperate dashboard
	if e_count > 0:
		return HttpResponseRedirect(reverse('editorsdesk_dashboard'))

	stories = MetaStory.objects.filter(created_by=request.user)
	entries = Media.children.filter(authors=request.user)

	return render_to_response("core/dashboard.html", {'stories':stories,'entries':entries}, context_instance=RequestContext(request))
 
@login_required
def user_profile(request):
	associated_openids = UserAssociation.objects.filter(user__id=request.user.id)
	if associated_openids.count() < 2:
		allow_delete = False
	else:
		allow_delete = True

	try: 
		profile = Profile.objects.get(user=request.user)
	except Profile.DoesNotExist:
		profile = Profile()

	return render_to_response("core/profile.html", {
		'associated_openids': associated_openids,
		'allow_delete' : allow_delete,
		'profile' : profile
	}, context_instance=RequestContext(request))

#@login_required
def save_profile(request):
	if request.method == 'POST':
		
		try: 
			profile = Profile.objects.get(user=request.user)
		except Profile.DoesNotExist:
			profile = Profile()
		
		profile.user = request.user
		profile.created_by = request.user
		profile.updated_by = request.user
		
		if (request.POST.get("gender") == '0'):
			profile.gender = 0;
		else:
			profile.gender = 1;
		
		form = ProfileForm(request.POST,instance=profile)
		
		if form.is_valid():
			form.save()
			request.user.message_set.create(message="1|Your profile was saved successfully.")

			return HttpResponseRedirect( reverse('user_profile') )
		else:
			request.user.message_set.create(message="0|An error has occured.")
			
			associated_openids = UserAssociation.objects.filter(user__id=request.user.id)
			if associated_openids.count() < 2:
				allow_delete = False
			else:
				allow_delete = True
			
			return render_to_response("core/profile.html", {
				'associated_openids': associated_openids,
				'allow_delete' : allow_delete,
				'profile' : profile,
				'errors' : form.errors
			}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )



@login_required
def user_association(request):
	newsrooms = Newsroom.objects.all()
	form = PartnerForm()
	return render_to_response("core/association.html", {'newsrooms':newsrooms,'form':form}, context_instance=RequestContext(request))

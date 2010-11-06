# -*- coding: utf-8 -*-
from django.contrib.auth.forms import *
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import datetime, md5, random, sys
from django_authopenid.forms import *
from django_authopenid.models import UserAssociation
from django.core.files.base import ContentFile
import django.contrib.auth.models as auth
from django.shortcuts import get_object_or_404

from news21national.core.models import Profile
from news21national.newsroom.models import Newsroom
from news21national.partner.models import Partner
from news21national.partner.forms import PartnerForm
from news21national.story.models import MetaStory, Story
from news21national.multimedia.models import Media
from news21national.api.models import Key as APIKey
from tagging.models import Tag, TaggedItem

@login_required
def create_partner_member(request):
	if request.method == 'POST':
		partner = Partner(created_by = request.user, updated_by = request.user)
		
		form = PartnerForm(request.POST,instance=partner)
		
		if form.is_valid():
			form.save()
			
			partner.members.add(request.user)
			
			request.user.message_set.create(message="1|Your partner info was saved successfully.")
			
			return HttpResponseRedirect( reverse('partner_dashboard') )
		else:
			request.user.message_set.create(message="0|An error has occured.")
			newsrooms = Newsroom.objects.all()
			
			return render_to_response( "main/association.html", {'newsrooms':newsrooms,'form':form}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )


@login_required
def dashboard(request):
	n = Newsroom.objects.all()
	t = Tag.objects.all()
	u = Profile.objects.filter(user__in=auth.User.objects.filter(newsroom_members__in=Newsroom.objects.values_list('id',flat=True)).distinct()).order_by('first_name').order_by('last_name')
	partners = Partner.objects.filter(members=request.user).distinct()
	return render_to_response( "partner/dashboard.html", {'newsrooms':n,'reporters':u,'categories':t,'partners':partners}, context_instance=RequestContext(request))


@login_required
def generate_api_key(request,partner_id):
	#make sure user is a member of the partner passed
	partners = Partner.objects.filter(members=request.user).distinct()
	for p in partners:
		if p.id == int(partner_id):
			partner = get_object_or_404(Partner, pk=partner_id)
			partner.get_keys().update(is_active=0)
			partner.add_key(request.user)
			break
	return HttpResponseRedirect( reverse('partner_dashboard') )

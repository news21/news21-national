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

from news21national.core.models import Profile, ProfileForm
from news21ams.newsroom.models import Newsroom
from news21ams.partner.models import Partner, PartnerForm
from news21ams.story.models import MetaStory
from news21ams.multimedia.models import Media

def home(request):
    return render_to_response("core/home.html", {}, context_instance=RequestContext(request))

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
    if n_count == 0 and p_count == 0:
        return HttpResponseRedirect(reverse('user_association'))
    
    # if user is part of a partner ... send to seperate dashboard
    if p_count > 0:
        return HttpResponseRedirect(reverse('partner_dashboard'))
    
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

    form = ProfileForm(instance=profile)

    return render_to_response("core/profile.html", {
        'associated_openids': associated_openids,
        'allow_delete' : allow_delete,
        'form': form,
    }, context_instance=RequestContext(request))

@login_required
def user_association(request):
    newsrooms = Newsroom.objects.all()
    form = PartnerForm()
    return render_to_response("core/association.html", {'newsrooms':newsrooms,'form':form}, context_instance=RequestContext(request))

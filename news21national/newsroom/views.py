# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime
from django.conf import settings
from news21national.newsroom.models import Newsroom

@login_required
def create_newsroom_member(request,newsroom_id):
	try: 
		n = Newsroom(pk=newsroom_id)
	except Newsroom.DoesNotExist:
		return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
	
	n.members.add(request.user)
	
	return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

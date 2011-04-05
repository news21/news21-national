from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required

from news21national.story.models import Story, MetaStory
from news21national.newsroom.models import Newsroom
from tagging.models import Tag
from news21national.core.models import Profile
import django.contrib.auth.models as auth

from operator import itemgetter

def filtered(request,filter_name):
	response_dict = {}
	stories = []
	for s in Story.objects.all().order_by('metastory'):
		st = dict(id=s.id,headline=s.headline,metastory=s.metastory,metastoryid=s.metastory.id,year=s.metastory.year_of_newsroom)
		stories.append( st )
	s = sorted(stories, key=itemgetter('year'))

	return render_to_response(
        "admin/story/filters_year.html",
        {'stories':s,'years':[10,9,8,7,6]},
        RequestContext(request, {}),
    )
filtered = staff_member_required(filtered)
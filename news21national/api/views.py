from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import get_object_or_404

from news21national.newsroom.models import Newsroom
from news21national.story.models import MetaStory, Story
from news21national.story.forms import MetaStoryForm, StoryForm
from news21national.multimedia.models import Media
from news21national.photos.models import Photo
from news21national.api.models import Key
from news21national.partner.models import StoryPlacements
from tagging.models import Tag,TaggedItem

from django.core import serializers


def story_categories(request,api_key,dif='json'):
	nl = []
	for n in Tag.objects.usage_for_model(Newsroom):
		nl.append(n.name)
	categories = Tag.objects.exclude(name__in=nl)

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)
	 
	return render_to_response('api/'+settings.API_VERSION+'/categories_'+dif+'.html', { 'categories': categories, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def stories_by_category(request,api_key,category_id,dif='json'):
	stories = TaggedItem.objects.get_by_model(Story, Tag.objects.get(name=category_id) )
	
	sids = []
	for i in stories.values_list('primary_image',flat=True):
		sids.append(i)
	photos = Media.children.filter(pk__in=sids,_child_name="photo",status="Approved")

	sarray = []
	for s in stories:
		for p in photos:
			if p.id is s.primary_image:
				sarray.append({ "slug":s.slug, "headline":s.headline, "summary":s.summary, "original_url":s.original_url, "primary_image": 'http://'+ request.get_host()+''+p.get_thumbnail_url(), "newsroom":category_id } )
	
	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)
	
	return render_to_response('api/'+settings.API_VERSION+'/stories_by_category_'+dif+'.html', { 'stories': sarray, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)

def story(request,api_key,story_id,dif='json',custom_filter=''):
	story = get_object_or_404(Story, pk=story_id)

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+settings.API_VERSION+'/story'+custom_filter+'_'+dif+'.html', { 'story': story, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def media(request,api_key,media_id,dif='json'):
	media = get_object_or_404(Media, pk=media_id)

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+settings.API_VERSION+'/media_'+dif+'.html', { 'media': media, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)

def newsrooms_categories(request,api_key,dif='json'):
	newsrooms = Tag.objects.usage_for_model(Newsroom)

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+settings.API_VERSION+'/newsrooms_'+dif+'.html', { 'newsrooms': newsrooms, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def newsrooms_bios(request,api_key,newsroom_id,dif='json'):
	n = get_object_or_404(Newsroom,pk=newsroom_id)
	bios = Profile.objects.filter(user__in=n.members.values_list('id',flat=True)).distinct().order_by('last_name')

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+settings.API_VERSION+'/newsroom_bios_'+dif+'.html', { 'bios': bios, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def bio(request,api_key,user_id,dif='json'):
	bio = Profile.objects.get(user_id=user_id)

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+settings.API_VERSION+'/bio_'+dif+'.html', { 'bio': bio, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def story_placements(request,api_key,story_id,dif='json'):
	story = get_object_or_404(Story, pk=story_id)
	placements = StoryPlacements.objects.filter(story=story)[5]
	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+settings.API_VERSION+'/story_placements_'+dif+'.html', { 'placements': placements, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)
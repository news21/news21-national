from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import django.contrib.auth.models as auth
from datetime import datetime
import time

from news21national.story.models import MetaStory, Story
from tagging.models import Tag
from geotagging.models import Geotag

from news21national.swfs.forms import SwfForm as MultimediaForm
from news21national.swfs.models import Swf as MultimediaModel

MULTIMEDIA_TYPE = 'swf'
MULTIMEDIA_TITLE = 'Flash SWF'
MULTIMEDIA_HTML = 'swf.html'

@login_required
def get_swf(request,metastory_id,story_id,multimedia_id=None):
	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	story = get_object_or_404(Story, pk=story_id, metastory=metastory)
	
	inherited_tags = []
	inherited_tag_ids = []
	for newsroom in metastory.newsrooms.all():
		for tag in newsroom.get_tags():
			inherited_tags.append(tag)
			inherited_tag_ids.append(tag.id)
	for mtag in metastory._get_tags():
		inherited_tags.append(mtag)
		inherited_tag_ids.append(mtag.id)
	for stag in story._get_tags():
		inherited_tags.append(stag)
		inherited_tag_ids.append(stag.id)
	tags = Tag.objects.exclude(id__in=inherited_tag_ids)
	
	members = metastory.get_members()
	
	if multimedia_id:
		multimedia = get_object_or_404(MultimediaModel, pk=multimedia_id, story=story)
		form = MultimediaForm(instance=multimedia)
		authors = multimedia.authors.all()
		used_tags = multimedia._get_tags()
		
		geotag = multimedia._get_geotag()
		
		multimedia_title = multimedia
		multimedia_url = reverse(MULTIMEDIA_TYPE+'_edit', args=[metastory_id,story_id,multimedia.id])
		form_url = reverse(MULTIMEDIA_TYPE+'_update', args=[metastory_id,story_id,multimedia.id])
	else:
		form = MultimediaForm()
		authors = []
		used_tags = []
		geotag = {}
		multimedia_title = 'New '+MULTIMEDIA_TITLE
		multimedia_url = reverse(MULTIMEDIA_TYPE+'_new', args=[metastory_id,story_id])
		form_url = reverse(MULTIMEDIA_TYPE+'_create', args=[metastory_id,story_id])
		
	breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia_title,'url':multimedia_url} ]
	return render_to_response("multimedia/"+MULTIMEDIA_HTML, {'breadcrumb':breadcrumb,'form':form,'authors':authors,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'geotag':geotag,'newsrooms_members':members,'form_url':form_url}, context_instance=RequestContext(request))


@login_required
def save_swf(request,metastory_id,story_id,multimedia_id=None):
	if request.method == 'POST':
		metastory= get_object_or_404(MetaStory, pk=metastory_id)
		story = get_object_or_404(Story, pk=story_id, metastory=metastory)

		if not multimedia_id:
			multimedia = MultimediaModel(created_by = request.user, story=story, created_at = datetime.now())
			multimedia_title = 'New '+MULTIMEDIA_TITLE
			multimedia_url = reverse(MULTIMEDIA_TYPE+'_new', args=[metastory_id,story_id])
			form_url = reverse(MULTIMEDIA_TYPE+'_create', args=[metastory_id,story_id])
		else:	 
			multimedia = get_object_or_404(MultimediaModel, pk=multimedia_id, story=story)
			multimedia_title = multimedia
			multimedia_url = reverse(MULTIMEDIA_TYPE+'_edit', args=[metastory_id,story_id,multimedia.id])
			form_url = reverse(MULTIMEDIA_TYPE+'_update', args=[metastory_id,story_id,multimedia.id])

		multimedia.updated_by = request.user
		multimedia.updated_at = datetime.now()
		form = MultimediaForm(request.POST, request.FILES,instance=multimedia)

		if form.is_valid():
			form.save()
			request.user.message_set.create(message="1|Your "+MULTIMEDIA_TYPE+" asset was saved successfully.")

			multimedia.authors = request.POST.getlist('authors')
			multimedia.process_zipfile()
			
			if request.POST.get("geo_tag_lat",None) is not None:
				point = Geotag(object=multimedia,point='SRID=4326;POINT ('+request.POST.get("geo_tag_lon")+' '+request.POST.get("geo_tag_lat")+')' )
				multimedia._remove_geotag()
				point.save()
			
			stags = ''
			for tag in Tag.objects.all():
				if request.POST.__contains__('tag_%d' % tag.id):
					stags += ' '+tag.name
			multimedia._set_tags(stags)
			
			return HttpResponseRedirect( reverse(MULTIMEDIA_TYPE+'_edit', args=[metastory_id,story_id,multimedia.id]) )
		else:
			request.user.message_set.create(message="0|An error has occured.")
			members = metastory.get_members()
			authors = []
			
			inherited_tags = []
			inherited_tag_ids = []
			for newsroom in metastory.newsrooms.all():
				for tag in newsroom.get_tags():
					inherited_tags.append(tag)
					inherited_tag_ids.append(tag.id)
			for mtag in metastory._get_tags():
				inherited_tags.append(mtag)
				inherited_tag_ids.append(mtag.id)
			for stag in story._get_tags():
				inherited_tags.append(stag)
				inherited_tag_ids.append(stag.id)
			tags = Tag.objects.exclude(id__in=inherited_tag_ids)
			used_tags = multimedia._get_tags()

			breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia_title,'url':multimedia_url} ]
			return render_to_response("multimedia/"+MULTIMEDIA_HTML, {'breadcrumb':breadcrumb,'form':form,'image':multimedia,'authors':authors,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'newsrooms_members':members,'form_url':form_url}, context_instance=RequestContext(request))
		
	else:
		return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
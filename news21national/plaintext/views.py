# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import django.contrib.auth.models as auth
from django.template.defaultfilters import slugify
from datetime import datetime

from news21national.editorsdesk.forms import EditorsCommentForm
from news21national.editorsdesk.models import EditorsDesk
from news21national.plaintext.forms import PlainTextForm
from news21national.plaintext.models import PlainText
from news21national.multimedia.models import Media
from news21national.story.models import MetaStory, Story

from tagging.models import Tag
from geotagging.models import Geotag


@login_required
def new_plaintext(request,metastory_id,story_id):
	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	story = get_object_or_404(Story, pk=story_id, metastory=metastory)
	multimedia = PlainText()
	multimedia.title = story.headline
	multimedia.summary = story.summary
	multimedia.slug = story.slug
	form = PlainTextForm(instance=multimedia)
	members = metastory.get_members()
	mediaclass = None
	editorcommentform = EditorsCommentForm()
	
	inherited_tags = []
	inherited_tag_ids = []
	for mtag in metastory._get_tags():
		inherited_tags.append(mtag)
		inherited_tag_ids.append(mtag.id)
	for stag in story._get_tags():
		if stag not in inherited_tags: inherited_tags.append(stag)
		if stag.id not in inherited_tag_ids: inherited_tag_ids.append(stag.id)
	tags = Tag.objects.exclude(id__in=inherited_tag_ids)
	
	breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':'New PlainText','url':reverse('plaintext_new', args=[metastory_id,story_id])} ]
	return render_to_response("multimedia/plaintext.html", {'breadcrumb':breadcrumb,'editorcommentform':editorcommentform,'mediaclass':mediaclass,'form':form,'newsrooms_members':members,'inherited_tags':inherited_tags,'tags':tags,'form_url':reverse('plaintext_create', args=[metastory_id,story_id])}, context_instance=RequestContext(request))


@login_required
def edit_plaintext(request,metastory_id,story_id,multimedia_id,template_name="multimedia/plaintext.html",is_editor=False):
	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	story = get_object_or_404(Story, pk=story_id, metastory=metastory)
	multimedia = get_object_or_404(PlainText, pk=multimedia_id, story=story)
	form = PlainTextForm(instance=multimedia)
	members = metastory.get_members()
	authors = multimedia.authors.all()
	mediaclass = get_object_or_404(Media, pk=multimedia_id)
	editorcommentform = EditorsCommentForm()
	
	if EditorsDesk.objects.filter(newsroom__in=metastory.newsrooms.values_list('id',flat=True),editors__in=[request.user]).count() > 0:
		is_editor = True
	
	geotag = multimedia._get_geotag()
	
	inherited_tags = []
	inherited_tag_ids = []
	for mtag in metastory._get_tags():
		inherited_tags.append(mtag)
		inherited_tag_ids.append(mtag.id)
	for stag in story._get_tags():
		if stag not in inherited_tags: inherited_tags.append(stag)
		if stag.id not in inherited_tag_ids: inherited_tag_ids.append(stag.id)
	tags = Tag.objects.exclude(id__in=inherited_tag_ids)
	used_tags = multimedia._get_tags()
	
	breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia,'url':reverse('plaintext_edit', args=[metastory_id,story_id,multimedia_id])} ]
	return render_to_response(template_name, {'breadcrumb':breadcrumb,'editorcommentform':editorcommentform,'google_maps_api_key':settings.GOOGLE_MAPS_API_KEY,'form':form,'newsrooms_members':members,'authors':authors,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'geotag':geotag,'status':multimedia.status,'form_url':reverse('plaintext_update', args=[metastory_id,story_id,multimedia_id]),'is_editor':is_editor,'mediaclass':mediaclass}, context_instance=RequestContext(request))


@login_required
def save_plaintext(request,metastory_id,story_id,multimedia_id=None):
	if request.method == 'POST':
		metastory= get_object_or_404(MetaStory, pk=metastory_id)
		story = get_object_or_404(Story, pk=story_id, metastory=metastory)
		if multimedia_id:
			multimedia = get_object_or_404(PlainText, pk=multimedia_id, story=story)
		else:
			multimedia = PlainText(created_by = request.user, story=story, created_at = datetime.now())

		multimedia.updated_by = request.user
		multimedia.updated_at = datetime.now()
		form = PlainTextForm(request.POST,instance=multimedia)
		
		if form.is_valid():
			form.save()
			request.user.message_set.create(message="1|Your plaintext asset was saved successfully.")
			
			multimedia.authors = request.POST.getlist('authors')
			
			if request.POST.get("geo_tag_lat",None) is not None:
				point = Geotag(tagged_obj=multimedia,point='SRID=4326;POINT ('+request.POST.get("geo_tag_lon")+' '+request.POST.get("geo_tag_lat")+')' )
				multimedia._remove_geotag()
				point.save()
			
			stags = ''
			for tag in Tag.objects.all():
				if request.POST.__contains__('tag_%d' % tag.id):
					stags += ' '+tag.name
			multimedia._set_tags(stags)
			
			return HttpResponseRedirect( reverse('plaintext_edit', args=[metastory_id,story_id,multimedia.id]) )
		else:
			request.user.message_set.create(message="0|An error has occured.")
			members = metastory.get_members()
			if multimedia_id:
				authors = multimedia.authors.all()
			else:
				authors = []
			
			inherited_tags = []
			inherited_tag_ids = []
			for mtag in metastory._get_tags():
				inherited_tags.append(mtag)
				inherited_tag_ids.append(mtag.id)
			for stag in story._get_tags():
				if stag not in inherited_tags: inherited_tags.append(stag)
				if stag.id not in inherited_tag_ids: inherited_tag_ids.append(stag.id)
			tags = Tag.objects.exclude(id__in=inherited_tag_ids)
			used_tags = multimedia._get_tags()

			breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia,'url':''} ]
			return render_to_response("multimedia/plaintext.html", {'breadcrumb':breadcrumb,'form':form,'newsrooms_members':members,'authors':authors,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'status':multimedia.status,'form_url':reverse('plaintext_update', args=[metastory_id,story_id,multimedia_id])}, context_instance=RequestContext(request))
			
	else:
		return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
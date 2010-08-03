from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import django.contrib.auth.models as auth
from datetime import datetime
import time
import sys

from news21national.editorsdesk.models import EditorsDesk
from news21national.story.models import MetaStory, Story
from tagging.models import Tag
from news21national.embed.forms import EmbedForm
from news21national.embed.models import Embed
from news21national.multimedia.models import Media

@login_required
def get_embed(request,metastory_id,story_id,multimedia_id=None,template_name="multimedia/embed.html",is_editor=False):
	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	story = get_object_or_404(Story, pk=story_id, metastory=metastory)
	
	inherited_tags = []
	inherited_tag_ids = []
	for mtag in metastory._get_tags():
		inherited_tags.append(mtag)
		inherited_tag_ids.append(mtag.id)
	for stag in story._get_tags():
		if stag not in inherited_tags: inherited_tags.append(stag)
		if stag.id not in inherited_tag_ids: inherited_tag_ids.append(stag.id)
	tags = Tag.objects.exclude(id__in=inherited_tag_ids)
	
	members = metastory.get_members()
	
	if multimedia_id:
		multimedia = get_object_or_404(Embed, pk=multimedia_id, story=story)
		mediaclass = get_object_or_404(Media, pk=multimedia_id)
		if EditorsDesk.objects.filter(newsroom__in=metastory.newsrooms.values_list('id',flat=True),editors__in=[request.user]).count() > 0:
			is_editor = True
		form = EmbedForm(instance=multimedia)
		authors = multimedia.authors.all()
		used_tags = multimedia._get_tags()
		multimedia_title = multimedia
		multimedia_url = reverse('embed_edit', args=[metastory_id,story_id,multimedia.id])
		form_url = reverse('embed_update', args=[metastory_id,story_id,multimedia.id])
		ctype = ContentType.objects.get_for_model(multimedia)
	else:
		multimedia = None
		mediaclass = None
		form = EmbedForm()
		authors = []
		used_tags = []
		multimedia_title = 'New Embed'
		multimedia_url = reverse('embed_new', args=[metastory_id,story_id])
		form_url = reverse('embed_create', args=[metastory_id,story_id])

	breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia_title,'url':multimedia_url} ]
	return render_to_response(template_name, {'breadcrumb':breadcrumb,'form':form,'embed':multimedia,'mediaclass':mediaclass,'authors':authors,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'newsrooms_members':members,'form_url':form_url,'is_editor':is_editor}, context_instance=RequestContext(request))


@login_required
def save_embed(request,metastory_id,story_id,multimedia_id=None):
	if request.method == 'POST':
		metastory= get_object_or_404(MetaStory, pk=metastory_id)
		story = get_object_or_404(Story, pk=story_id, metastory=metastory)
		
		if not multimedia_id:
			multimedia = Embed(created_by = request.user, story=story, created_at = datetime.now())
			multimedia_title = 'New Embed'
			multimedia_url = reverse('embed_new', args=[metastory_id,story_id])
			form_url = reverse('embed_create', args=[metastory_id,story_id])
		else:
			multimedia = get_object_or_404(Embed, pk=multimedia_id, story=story)
			multimedia_title = multimedia
			multimedia_url = reverse('embed_edit', args=[metastory_id,story_id,multimedia.id])
			form_url = reverse('embed_update', args=[metastory_id,story_id,multimedia.id])
			
			
		multimedia.updated_by = request.user
		multimedia.updated_at = datetime.now()
		form = EmbedForm(request.POST,instance=multimedia)
		
		members = metastory.get_members()
		
		if form.is_valid():
			form.save()
			request.user.message_set.create(message="1|Your embed asset was saved successfully.")
		
			multimedia.authors = request.POST.getlist('authors')
				
			stags = ''
			for tag in Tag.objects.all():
				if request.POST.__contains__('tag_%d' % tag.id):
					stags += ' '+tag.name
			multimedia._set_tags(stags)
			
			return HttpResponseRedirect( reverse('embed_edit', args=[metastory_id,story_id,multimedia.id]) )
		else:
			request.user.message_set.create(message="0|An error has occured.")
			authors = []
			
			inherited_tags = []
			inherited_tag_ids = []
			for mtag in metastory._get_tags():
				inherited_tags.append(mtag)
				inherited_tag_ids.append(mtag.id)
			for stag in story._get_tags():
				inherited_tags.append(stag)
				inherited_tag_ids.append(stag.id)
			tags = Tag.objects.exclude(id__in=inherited_tag_ids)	
			used_tags = multimedia._get_tags()

		members = metastory.get_members()
		breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia_title,'url':multimedia_url} ]
		return render_to_response("multimedia/embed.html", {'breadcrumb':breadcrumb,'form':form,'embed':multimedia,'authors':authors,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'newsrooms_members':members,'form_url':form_url}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
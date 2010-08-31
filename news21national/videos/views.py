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

from news21national.editorsdesk.forms import EditorsCommentForm
from news21national.editorsdesk.models import EditorsDesk
from news21national.story.models import MetaStory, Story
from tagging.models import Tag
from geotagging.models import Geotag
from news21national.multimedia.models import Media
from news21national.videos.forms import VideoForm
from news21national.videos.models import Video


@login_required
def get_video(request,metastory_id,story_id,multimedia_id=None,template_name="multimedia/video.html",is_editor=False):
	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	story = get_object_or_404(Story, pk=story_id, metastory=metastory)
	mediaclass = get_object_or_404(Media, pk=multimedia_id)
	
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
		multimedia = get_object_or_404(Video, pk=multimedia_id, story=story)
		mediaclass = get_object_or_404(Media, pk=multimedia_id)
		form = VideoForm(instance=multimedia)
		authors = multimedia.authors.all()
		used_tags = multimedia._get_tags()
		
		geotag = multimedia._get_geotag()
		
		multimedia_title = multimedia
		multimedia_url = reverse('video_edit', args=[metastory_id,story_id,multimedia.id])
		form_url = reverse('video_update', args=[metastory_id,story_id,multimedia.id])
		if EditorsDesk.objects.filter(newsroom__in=metastory.newsrooms.values_list('id',flat=True),editors__in=[request.user]).count() > 0:
			is_editor = True
	else:
		multimedia = Video(story=story)
		mediaclass = None
		form = VideoForm()
		authors = []
		used_tags = []
		geotag = {}
		multimedia_title = 'New Video'
		multimedia_url = reverse('video_new', args=[metastory_id,story_id])
		form_url = reverse('video_create', args=[metastory_id,story_id])
		
	breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia_title,'url':multimedia_url} ]
	return render_to_response(template_name, {'breadcrumb':breadcrumb,'multimedia':multimedia,'google_maps_api_key':settings.GOOGLE_MAPS_API_KEY,'form':form,'authors':authors,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'geotag':geotag,'newsrooms_members':members,'form_url':form_url,'is_editor':is_editor,'mediaclass':mediaclass}, context_instance=RequestContext(request))


@login_required
def save_video(request,metastory_id,story_id,multimedia_id=None):
	if request.method == 'POST':
		metastory= get_object_or_404(MetaStory, pk=metastory_id)
		story = get_object_or_404(Story, pk=story_id, metastory=metastory)

		if not multimedia_id:
			multimedia = Video(created_by = request.user, story=story, created_at = datetime.now())
			multimedia_title = 'New Video'
			multimedia_url = reverse('video_new', args=[metastory_id,story_id])
			form_url = reverse('video_create', args=[metastory_id,story_id])
		else:	 
			multimedia = get_object_or_404(Video, pk=multimedia_id, story=story)
			multimedia_title = multimedia
			multimedia_url = reverse('video_edit', args=[metastory_id,story_id,multimedia.id])
			form_url = reverse('video_update', args=[metastory_id,story_id,multimedia.id])

		multimedia.updated_by = request.user
		multimedia.updated_at = datetime.now()
		form = VideoForm(request.POST, request.FILES,instance=multimedia)

		if form.is_valid():
			form.save()
			request.user.message_set.create(message="1|Your video asset was saved successfully.")

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
			
			return HttpResponseRedirect( reverse('video_edit', args=[metastory_id,story_id,multimedia.id]) )
		else:
			request.user.message_set.create(message="0|An error has occured.")
			members = metastory.get_members()
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

			breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia_title,'url':multimedia_url} ]
			return render_to_response("multimedia/video.html", {'breadcrumb':breadcrumb,'form':form,'image':multimedia,'authors':authors,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'newsrooms_members':members,'form_url':form_url}, context_instance=RequestContext(request))
		
	else:
		return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
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

from news21national.editorsdesk.forms import EditorsCommentForm
from news21national.editorsdesk.models import EditorsDesk
from news21national.story.models import MetaStory, Story
from tagging.models import Tag
from geotagging.models import Geotag
from news21national.photos.forms import PhotoForm, ImageForm
from news21national.photos.models import Photo
from news21national.multimedia.models import Media
from news21national.socialchecklist.models import Payload, Outlet

@login_required
def get_photo(request,metastory_id,story_id,multimedia_id=None,template_name="multimedia/photo.html",is_editor=False):
	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	story = get_object_or_404(Story, pk=story_id, metastory=metastory)
	flickr_outlet = Outlet.objects.get(name='Flickr')
	
	inherited_tags = []
	inherited_tag_ids = []
	for mtag in metastory._get_tags():
		inherited_tags.append(mtag)
		inherited_tag_ids.append(mtag.id)
	for stag in story._get_tags():
		if stag not in inherited_tags: inherited_tags.append(stag)
		if stag.id not in inherited_tag_ids: inherited_tag_ids.append(stag.id)
	tags = Tag.objects.exclude(id__in=inherited_tag_ids)
	
	upload_form = ImageForm()
	members = metastory.get_members()
	editorcommentform = EditorsCommentForm()
	
	if multimedia_id:
		multimedia = get_object_or_404(Photo, pk=multimedia_id, story=story)
		mediaclass = get_object_or_404(Media, pk=multimedia_id)
		#geotag = multimedia._get_geotag()
		if EditorsDesk.objects.filter(newsroom__in=metastory.newsrooms.values_list('id',flat=True),editors__in=[request.user]).count() > 0:
			is_editor = True
		
		geotag = multimedia._get_geotag()
		
		form = PhotoForm(instance=multimedia)
		authors = multimedia.authors.all()
		used_tags = multimedia._get_tags()
		multimedia_title = multimedia
		multimedia_url = reverse('photo_edit', args=[metastory_id,story_id,multimedia.id])
		form_url = reverse('photo_update', args=[metastory_id,story_id,multimedia.id])
		upload_form_url = ''
		ctype = ContentType.objects.get_for_model(multimedia)
		try:
			flickr_payload = Payload.objects.get(outlet=flickr_outlet, object_id=multimedia.id,content_type=ctype)
		except Payload.DoesNotExist:
			flickr_payload = Payload()
	else:
		multimedia = None
		mediaclass = None
		geotag = {}
		flickr_payload = Payload()
		form = PhotoForm()
		authors = []
		used_tags = []
		multimedia_title = 'New Photo'
		multimedia_url = reverse('photo_new', args=[metastory_id,story_id])
		form_url = ''
		upload_form_url = reverse('photo_create', args=[metastory_id,story_id])

	breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia_title,'url':multimedia_url} ]
	return render_to_response(template_name, {'breadcrumb':breadcrumb,'editorcommentform':editorcommentform,'form':form,'image':multimedia,'mediaclass':mediaclass,'authors':authors,'upload_form':upload_form,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'geotag':geotag,'newsrooms_members':members,'form_url':form_url,'upload_form_url':upload_form_url,'flickr_payload':flickr_payload,'google_maps_api_key':settings.GOOGLE_MAPS_API_KEY,'is_editor':is_editor}, context_instance=RequestContext(request))


@login_required
def save_photo(request,metastory_id,story_id,multimedia_id=None):
	if request.method == 'POST':
		metastory= get_object_or_404(MetaStory, pk=metastory_id)
		story = get_object_or_404(Story, pk=story_id, metastory=metastory)
		flickr_outlet = Outlet.objects.get(name='Flickr')
		saveSocial = False
		form = PhotoForm()
		upload_form = ImageForm(request.POST, request.FILES)
		if not multimedia_id:
			if upload_form.is_valid():
				multimedia = Photo(created_by = request.user, story=story, created_at = datetime.now())
				image = upload_form.save()
				
				multimedia.updated_by = request.user
				multimedia.updated_at = datetime.now()
				
				multimedia.title = image.image.name
				
				multimedia.summary = image.image.name
				try:
					multimedia.summary = image.MinimalEXIF().imageDescription()
				except:
					multimedia.summary = image.image.name
				
				if image.EXIF().has_key("EXIF DateTimeOriginal"):
					dt = datetime.strptime(str(image.MinimalEXIF().dateTimeOriginal()), '%Y:%m:%d %H:%M:%S').timetuple()
					multimedia.date_taken = datetime(*dt[0:6])
				
				multimedia.image = image
				multimedia.save()
				
				# save flickr info
				saveSocial = True
				
				form = PhotoForm(instance=multimedia)
			else:
				emsg = ''
				for value in upload_form.errors:
					emsg +=' '+value+' '+str(upload_form.errors[value])
				request.user.message_set.create(message="0|A file is required for upload."+emsg)
				return HttpResponseRedirect( reverse('photo_new', args=[metastory_id,story_id]) )
		else:	 
			multimedia = get_object_or_404(Photo, pk=multimedia_id, story=story)
			image_url = multimedia.image.image.name
			multimedia.updated_by = request.user
			multimedia.updated_at = datetime.now()
			multimedia.authors = request.POST.getlist('authors')
			form = PhotoForm(request.POST,instance=multimedia)

			if form.is_valid():
				form.save()
				request.user.message_set.create(message="1|Your photo asset was saved successfully.")
				
				# save flickr info
				saveSocial = True
				
				
				if request.POST.get("geo_tag_lat",None) is not None:
					point = Geotag(tagged_obj=multimedia,point='SRID=4326;POINT ('+request.POST.get("geo_tag_lon")+' '+request.POST.get("geo_tag_lat")+')' )
					multimedia._remove_geotag()
					point.save()
				
				stags = ''
				for tag in Tag.objects.all():
					if request.POST.__contains__('tag_%d' % tag.id):
						stags += ' '+tag.name
				multimedia._set_tags(stags)
				
			else:
				request.user.message_set.create(message="0|An error has occured.")
		
		flickr_payload = {}
		if saveSocial:
			ctype = ContentType.objects.get_for_model(multimedia)
			# first check to see if there is already an instance
			try:
				flickr_payload = Payload.objects.get(outlet=flickr_outlet,object_id=multimedia.id,content_type=ctype)
			except Payload.DoesNotExist:
				flickr_payload = Payload(outlet=flickr_outlet, object_id=multimedia.id,content_type=ctype, created_by=request.user,created_at=datetime.now())
			
			flickr_payload.updated_by=request.user
			flickr_payload.updated_at=datetime.now()
			flickr_payload.blurb = request.POST.get('flickr_description')
			
			if request.POST.get('flickr_placement_url') is not None:
				flickr_payload.placement_url = request.POST.get('flickr_placement_url')
				flickr_payload.placed_at = datetime.now()
				flickr_payload.placed_by = request.user
			
			flickr_payload.save()
		
		authors = multimedia.authors.all()
		
		geotag = multimedia._get_geotag()
		
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

		members = metastory.get_members()
		breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} , {'title':multimedia,'url':reverse('photo_edit', args=[metastory_id,story_id,multimedia.id])} ]
		return render_to_response("multimedia/photo.html", {'breadcrumb':breadcrumb,'form':form,'image':multimedia,'upload_form':upload_form,'authors':authors,'inherited_tags':inherited_tags,'tags':tags,'used_tags':used_tags,'newsrooms_members':members,'form_url':reverse('photo_update', args=[metastory_id,story_id,multimedia.id]),'upload_form_url':'','flickr_payload':flickr_payload,'geotag':geotag}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
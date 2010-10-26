from datetime import datetime
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import django.contrib.auth.models as auth
from django.template.defaultfilters import slugify

from news21national.editorsdesk.forms import EditorsCommentForm
from news21national.editorsdesk.models import EditorsDesk
from news21national.newsroom.models import Newsroom
from news21national.story.models import MetaStory, Story, StoryPublishDate
from news21national.story.forms import MetaStoryForm, StoryForm, StoryPublishDateForm
from news21national.multimedia.models import Media
from news21national.photos.models import Photo
from news21national.coderepo.models import CodeRepo
from tagging.models import Tag, TaggedItem
from news21national.socialchecklist.models import Payload, Outlet
from news21national.utils.nginx_rewrites import NginxRewrites

@login_required
def get_metastory(request,metastory_id=None,template_name="story/metastory.html",is_editor=False):
	tags = Tag.objects.all()
	
	primary_image = {}
	secondary_image = {}
	site_photos = []
	editorcommentform = EditorsCommentForm()
	
	if metastory_id:
		metastory = get_object_or_404(MetaStory, pk=metastory_id)
		
		if EditorsDesk.objects.filter(newsroom__in=metastory.newsrooms.values_list('id',flat=True),editors__in=[request.user]).count() > 0:
			is_editor = True
		form = MetaStoryForm(instance=metastory)
		stories = Story.objects.filter(metastory__id=metastory_id).order_by('headline')
		used_tags = metastory._get_tags()
		story_photos = Media.children.filter(story__in=stories.values_list('id',flat=True),_child_name="photo",status="Approved")
		site_photos = story_photos
		metastory_url = reverse('metastory_edit', args=[metastory_id])
		metastory_title = metastory
		geotags = metastory._get_geotags()
		form_url = reverse('metastory_update', args=[metastory_id])
		if metastory.primary_image is not None:
			story_photos = story_photos.exclude(pk=metastory.primary_image)
			primary_image = Photo.objects.get(pk=metastory.primary_image)
		if metastory.secondary_image is not None:
			site_photos = story_photos.exclude(pk=metastory.secondary_image)
			secondary_image = Photo.objects.get(pk=metastory.secondary_image)
		repos = CodeRepo.objects.get_for_object(metastory)
		audit = {"created_by":metastory.created_by,"created_at":metastory.created_at,"updated_by":metastory.updated_by,"updated_at":metastory.updated_at}
	else:
		metastory = MetaStory(created_by = request.user)
		form = MetaStoryForm()
		metastory_url = reverse('metastory_new')
		metastory_title = 'New Package'
		form_url = reverse('metastory_create')
		stories = []
		geotags = []
		used_tags = []
		story_photos = []
		repos = []
		audit = {}
		
	breadcrumb = [ {'title':metastory_title,'url':metastory_url} ]
	return render_to_response(template_name, {'primary_image':primary_image,'secondary_image':secondary_image,'editorcommentform':editorcommentform,'breadcrumb':breadcrumb,'form':form,'tags':tags,'used_tags':used_tags,'form_url':form_url,'stories':stories,'metastory_id':metastory_id,'story_photos':story_photos,'site_photos':site_photos,'repos':repos,'google_maps_api_key':settings.GOOGLE_MAPS_API_KEY,'audit':audit,'metastory':metastory,'is_editor':is_editor,'geotags':geotags}, context_instance=RequestContext(request))


@login_required
def save_metastory(request, metastory_id=None):
	if request.method == 'POST':
		if metastory_id:
			metastory = get_object_or_404(MetaStory, pk=metastory_id)
		else:
			metastory = MetaStory(created_by = request.user)
		
		metastory.primary_image = request.POST.get("primary_image",None)
		metastory.secondary_image = request.POST.get("secondary_image",None)
		#print request.POST.get("secondary_image",None)
		metastory.updated_by = request.user
		form = MetaStoryForm(request.POST,instance=metastory)

		if form.is_valid():
			form.save()
			request.user.message_set.create(message="1|Your meta-story was saved successfully.")
			
			mstags = ''
			for tag in Tag.objects.all():
				if request.POST.__contains__('tag_%d' % tag.id):
					mstags += ' '+tag.name
			metastory._set_tags(mstags)
			
			return HttpResponseRedirect( reverse('metastory_edit', args=[metastory.id]) )
		else:
			request.user.message_set.create(message="0|An error has occured.")
			
			tags = Tag.objects.all()
			return render_to_response( "story/metastory.html", {'form':form,'tags':tags}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )



@login_required
def get_story(request,metastory_id,story_id=None,template_name="story/story.html",is_editor=False):
	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	twitter_outlet = Outlet.objects.get(name='Twitter')
	facebook_outlet = Outlet.objects.get(name='Facebook')
	upiu_outlet = Outlet.objects.get(name='UPIU')
	
	inherited_tags = []
	inherited_tag_ids = []
	for mtag in metastory._get_tags():
		inherited_tags.append(mtag)
		inherited_tag_ids.append(mtag.id)
	tags = Tag.objects.exclude(id__in=inherited_tag_ids)
	
	primary_image = {}
	secondary_image = {}
	site_photos = []
	members = metastory.get_members()
	pubdateform = StoryPublishDateForm()
	editorcommentform = EditorsCommentForm()
	
	if story_id:
		story = get_object_or_404(Story, pk=story_id, metastory=metastory)
		
		if EditorsDesk.objects.filter(newsroom__in=metastory.newsrooms.values_list('id',flat=True),editors__in=[request.user]).count() > 0:
			is_editor = True
		
		form = StoryForm(instance=story)
		assets = Media.children.filter(story=story)
		authors = story.authors.all()
		photos = story.authors.all()
		story_photos = Media.children.filter(story=story,_child_name="photo",status="Approved")
		story_pubdates = StoryPublishDate.objects.filter(story=story)
		used_tags = story._get_tags()
		story_title = story
		geotags = story._get_geotags()
		story_url = reverse('story_edit', args=[metastory_id,story_id])
		form_url = reverse('story_update', args=[metastory_id,story_id])
		if story.primary_image is not None:
			story_photos = story_photos.exclude(pk=story.primary_image)
			primary_image = Photo.objects.get(pk=story.primary_image)
		if story.secondary_image is not None:
			site_photos = story_photos.exclude(pk=story.secondary_image)
			secondary_image = Photo.objects.get(pk=story.secondary_image)
		try:
			twitter_payload = Payload.objects.get_for_object(story,twitter_outlet)
		except Payload.DoesNotExist:
			twitter_payload = Payload()
		try:
			facebook_payload = Payload.objects.get_for_object(story,facebook_outlet)
		except Payload.DoesNotExist:
			facebook_payload = Payload()
		try:
			upiu_payload = Payload.objects.get_for_object(story,upiu_outlet)
		except Payload.DoesNotExist:
			upiu_payload = Payload()
		audit = {"created_by":metastory.created_by,"created_at":metastory.created_at,"updated_by":metastory.updated_by,"updated_at":metastory.updated_at}
	else:
		story = Story()
		form = StoryForm()
		assets = []
		authors = []
		photos = []
		story_photos = []
		story_pubdates = []
		used_tags = []
		geotags = []
		story_title = 'New Story'
		story_url = reverse('story_new', args=[metastory_id])
		form_url = reverse('story_create', args=[metastory_id])
		twitter_payload = Payload()
		facebook_payload = Payload()
		upiu_payload = Payload()
		audit = {}
	
	breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story_title,'url':story_url} ]
	return render_to_response(template_name, {'primary_image':primary_image,'pubdateform':pubdateform,'editorcommentform':editorcommentform,'secondary_image':secondary_image,'used_tags':used_tags,'inherited_tags':inherited_tags,'authors':authors,'media_assets':assets,'story':story,'story_id':story_id,'story_photos':story_photos,'breadcrumb':breadcrumb,'form':form,'newsrooms_members':members,'tags':tags,'form_url':form_url,'metastory_id':metastory_id,'story_pubdates':story_pubdates,'twitter_payload':twitter_payload,'facebook_payload':facebook_payload,'upiu_payload':upiu_payload,'google_maps_api_key':settings.GOOGLE_MAPS_API_KEY,'audit':audit,'is_editor':is_editor,'site_photos':site_photos,'geotags':geotags}, context_instance=RequestContext(request))


@login_required
def save_story(request,metastory_id,story_id=None):
	twitter_outlet = Outlet.objects.get(name='Twitter')
	facebook_outlet = Outlet.objects.get(name='Facebook')
	upiu_outlet = Outlet.objects.get(name='UPIU')
	if request.method == 'POST':
		metastory= get_object_or_404(MetaStory, pk=metastory_id)
		if story_id:
			story = get_object_or_404(Story, pk=story_id, metastory=metastory)
		else:
			story = Story(created_by = request.user, metastory=metastory)

		story.primary_image = request.POST.get("primary_image",None)
		story.updated_by = request.user
		form = StoryForm(request.POST,instance=story)
		
		if form.is_valid():
			form.save()
			
			# will need expanded on to filter by year and also seperate rewrite file by year
			rstories = Story.objects.filter(status="Approved").order_by('metastory')
			rewrites = []
			for r in rstories:
				for n in r.newsroom_shortcodes:
					if r.original_url != '':
						rewrites.append({"from":"/"+str(n)+""+str(r.id),"to":str(r.original_url)})
			#rewrites = [,{"from":"/nat/456","to":"http://national.news21.com"}]
			NginxRewrites().generate_conf(rewrites)
			
			ctype = ContentType.objects.get_for_model(story)
			try:
				twitter_payload = Payload.objects.get(outlet=twitter_outlet,object_id=story.id,content_type=ctype)
			except Payload.DoesNotExist:
				twitter_payload = Payload(outlet=twitter_outlet, object_id=story.id,content_type=ctype, created_by=request.user,created_at=datetime.now())
			twitter_payload.blurb = request.POST.get('twitter_description')

			try:
				facebook_payload = Payload.objects.get(outlet=facebook_outlet, object_id=story.id,content_type=ctype)
			except Payload.DoesNotExist:
				facebook_payload = Payload(outlet=facebook_outlet, object_id=story.id,content_type=ctype, created_by=request.user,created_at=datetime.now())
			facebook_payload.blurb = request.POST.get('facebook_description')

			try:
				upiu_payload = Payload.objects.get(outlet=upiu_outlet, object_id=story.id,content_type=ctype)
			except Payload.DoesNotExist:
				upiu_payload = Payload(outlet=upiu_outlet, object_id=story.id,content_type=ctype, created_by=request.user,created_at=datetime.now())
			upiu_payload.blurb = request.POST.get('upiu_description')
			
			twitter_payload.updated_by=request.user
			twitter_payload.updated_at=datetime.now()
			twitter_payload.save()
			
			facebook_payload.updated_by=request.user
			facebook_payload.updated_at=datetime.now()
			facebook_payload.save()
			
			upiu_payload.updated_by=request.user
			upiu_payload.updated_at=datetime.now()
			upiu_payload.save()
			
			story.authors = request.POST.getlist('authors')
			request.user.message_set.create(message="1|Your story was saved successfully.")
			
			stags = ''
			for tag in Tag.objects.all():
				if request.POST.__contains__('tag_%d' % tag.id):
					stags += ' '+tag.name
			story._set_tags(stags)
			
			return HttpResponseRedirect( reverse('story_edit', args=[metastory_id,story.id]) )
		else:
			request.user.message_set.create(message="0|An error has occured.")
			
			assets = Media.children.filter(story=story)
			members = metastory.get_members()
			authors = request.POST.getlist('authors')

			inherited_tags = []
			inherited_tag_ids = []
			for mtag in metastory._get_tags():
				inherited_tags.append(mtag)
				inherited_tag_ids.append(mtag.id)
			tags = Tag.objects.exclude(id__in=inherited_tag_ids)
			used_tags = []
			for tag in Tag.objects.all():
				if request.POST.__contains__('tag_%d' % tag.id):
					used_tags.append(tag)
			
			try:
				twitter_payload = Payload.objects.get_for_object(story,twitter_outlet)
			except Payload.DoesNotExist:
				twitter_payload = Payload()
			try:
				facebook_payload = Payload.objects.get_for_object(story,facebook_outlet)
			except Payload.DoesNotExist:
				facebook_payload = Payload()
			try:
				upiu_payload = Payload.objects.get_for_object(story,upiu_outlet)
			except Payload.DoesNotExist:
				upiu_payload = Payload()
			
			if story_id:
				breadcrumb = [ {'title':story.metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':story,'url':reverse('story_edit', args=[metastory_id,story_id])} ]
				form_url = reverse('story_update', args=[metastory_id,story_id])
			else:
				breadcrumb = [ {'title':story.metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':'New Story','url':reverse('story_new', args=[metastory_id])} ]
				form_url = reverse('story_create', args=[metastory_id])
			return render_to_response("story/story.html", {'breadcrumb':breadcrumb,'form':form,'newsrooms_members':members,'authors':authors,'media_assets':assets,'tags':tags,'used_tags':used_tags,'form_url':form_url,'metastory_id':metastory_id,'story_id':story_id,'inherited_tags':inherited_tags,'twitter_payload':twitter_payload,'facebook_payload':facebook_payload,'upiu_payload':upiu_payload}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

@login_required
def save_publishdate(request,metastory_id,story_id):
	response_dict = {}
	
	if request.method == 'POST':
		metastory= get_object_or_404(MetaStory, pk=metastory_id)
		story = get_object_or_404(Story, pk=story_id, metastory=metastory)
		publishdate = StoryPublishDate(created_by = request.user, updated_by = request.user, story=story)
		
		if request.POST.get("title",None) is None or request.POST.get("available_at",None) is None or request.POST.get("expires_at",None) is None:
			response_dict.update({'success': False})
		else:
			publishdate.title = request.POST.get("title",None)
			
			ad = request.POST.__getitem__("available_at").split('/')
			publishdate.available_at = datetime(int(ad[2]),int(ad[0]),int(ad[1]))
			
			ed = request.POST.__getitem__("expires_at").split('/')
			publishdate.expires_at = datetime(int(ed[2]),int(ed[0]),int(ed[1]))

			publishdate.save()
			response_dict.update({'success': True, 'pid': publishdate.id})
	else:
		response_dict.update({'success': False})
	
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')

@login_required
def remove_publishdate(request,metastory_id,story_id,publish_id):
	response_dict = {}
	
	if request.method == 'GET':
		try:
			metastory= get_object_or_404(MetaStory, pk=metastory_id)
			story = get_object_or_404(Story, pk=story_id, metastory=metastory)
			publishdate = get_object_or_404(StoryPublishDate, pk=publish_id, story=story)
		except:
			response_dict.update({'success': False})
		
		publishdate.delete()
		response_dict.update({'success': True})
		
	else:
		response_dict.update({'success': False})
	
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')

@login_required
def get_metastory_status(request,metastory_id,template_name="story/story_status.html"):
	response_dict = {}

	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	stories = Story.objects.filter(metastory__id=metastory_id).order_by('headline')
	assets = Media.children.filter(story__in=stories.values_list('id',flat=True))
	
	breadcrumb = [ {'title':metastory,'url':reverse('metastory_edit', args=[metastory_id])} , {'title':'Bulk Status','url':''} ]
	return render_to_response(template_name, {'breadcrumb':breadcrumb,'metastory':metastory,'stories':stories,'assets':assets}, context_instance=RequestContext(request))



def get_story_shorturls(request,template_name="story/shorturls.html"):
	rstories = Story.objects.filter(status="Approved").order_by('metastory')
	rewrites = []
	for r in rstories:
		for n in r.newsroom_shortcodes:
			if r.original_url != '':
				rewrites.append({"from":"/"+str(n)+""+str(r.id),"to":str(r.original_url),"metastory":str(r.metastory),"story":str(r)})
	return render_to_response(template_name, {'urls':rewrites}, context_instance=RequestContext(request))
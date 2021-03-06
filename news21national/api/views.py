from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import get_object_or_404

from news21national.awards.models import Award
from news21national.newsroom.models import Newsroom, NewsOrganization
from news21national.story.models import Project, MetaStory, Story
from news21national.story.forms import MetaStoryForm, StoryForm
from news21national.multimedia.models import Media
from news21national.photos.models import Photo
from news21national.core.models import Profile
from news21national.api.models import Key
from news21national.partner.models import StoryPlacements, Partner
from tagging.models import Tag,TaggedItem

from django.core import serializers
from django.db.models import Q


def story_categories(request,api_key,dif='json',version=settings.API_VERSION):
	nl = []
	for n in Tag.objects.usage_for_model(Newsroom):
		nl.append(n.name)
	categories = Tag.objects.exclude(name__in=nl)

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)
	 
	return render_to_response('api/'+version+'/categories_'+dif+'.html', { 'categories': categories, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def stories_by_category(request,api_key,category_id,dif='json',version=settings.API_VERSION):
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
	
	return render_to_response('api/'+version+'/stories_by_category_'+dif+'.html', { 'stories': sarray, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def stories_by_filters(request,api_key,dif='json',version=settings.API_VERSION):
	if request.method == 'POST':
		tags_filter = []
		newsrooms_filter = []
		assettypes_filter = []
		
		if len(request.POST.get("tags",'')) != 0:
			tags_filter = request.POST.get("tags",'').split(',')
		if len(request.POST.get("newsrooms",'')) != 0:
			newsrooms_filter = request.POST.get("newsrooms",'').split(',')
		if len(request.POST.get("assettypes",'')) != 0:
			assettypes_filter = request.POST.get("assettypes",'').split(',')
		
		sids = []
		sarray = []
		
		if len(tags_filter) >0:
			stories = TaggedItem.objects.get_by_model(Story, Tag.objects.filter(name__in=tags_filter) )
			metastories = TaggedItem.objects.get_by_model(MetaStory, Tag.objects.filter(name__in=tags_filter))
			ms = []
			for msvl in metastories.values_list('id',flat=True):
				ms.append(msvl)
			inheritstories = Story.objects.filter(metastory__id__in=ms)
			
			for i in stories.values_list('primary_image',flat=True):
				sids.append(i)
			for i2 in inheritstories.values_list('primary_image',flat=True):
				sids.append(i2)
			
			for s in stories:
				purl = ''
				for p in Media.children.filter(pk__in=sids,_child_name="photo",status="Approved"):
					if p.id is s.primary_image:
						purl = 'http://'+ request.get_host()+''+p.get_thumbnail_url()
				sarray.append({ "slug":s.slug, "year":s.created_at.year, "newsrooms":s.newsrooms, "headline":s.headline, "summary":s.summary, "original_url":s.original_url, "primary_image": purl, "id":s.id })
			
			for s2 in inheritstories:
				#first check to make sure inherited story is not already in array
				bfound = False
				for sa in sarray:
					#print sa
					if sa['id'] is s2.id:
						bfound = True
				if not bfound:
					purl = ''
					for p in Media.children.filter(pk__in=sids,_child_name="photo",status="Approved"):
						if p.id is s2.primary_image:
							purl = 'http://'+ request.get_host()+''+p.get_thumbnail_url()
					sarray.append({ "slug":s2.slug, "year":s2.created_at.year, "newsrooms":s2.newsrooms, "headline":s2.headline, "summary":s2.summary, "original_url":s2.original_url, "primary_image": purl, "id":s2.id })
		
		
		if len(newsrooms_filter) != 0:
			newroom_stories = Story.objects.filter(metastory__in=MetaStory.objects.filter(newsrooms__in=newsrooms_filter))
			for i3 in newroom_stories.values_list('primary_image',flat=True):
				sids.append(i3)
			
			for s3 in newroom_stories:
				#first check to make sure inherited story is not already in array
				bfound = False
				for sa in sarray:
					#print sa
					if sa['id'] is s3.id:
						bfound = True
				if not bfound:
					purl = ''
					for p in Media.children.filter(pk__in=sids,_child_name="photo",status="Approved"):
						if p.id is s3.primary_image:
							purl = 'http://'+ request.get_host()+''+p.get_thumbnail_url()
					sarray.append({ "slug":s3.slug, "year":s3.created_at.year, "newsrooms":s3.newsrooms, "headline":s3.headline, "summary":s3.summary, "original_url":s3.original_url, "primary_image": purl, "id":s3.id })
		
		
		if len(assettypes_filter) >0:
			assets_stories = Story.objects.filter(pk__in=Media.objects.filter(_child_name__in=assettypes_filter).values_list('story',flat=True))
			for i4 in assets_stories.values_list('primary_image',flat=True):
				sids.append(i4)
			for s4 in assets_stories:
				#first check to make sure inherited story is not already in array
				bfound = False
				for sa in sarray:
					#print sa
					if sa['id'] is s4.id:
						bfound = True
				if not bfound:
					purl = ''
					for p in Media.children.filter(pk__in=sids,_child_name="photo",status="Approved"):
						if p.id is s4.primary_image:
							purl = 'http://'+ request.get_host()+''+p.get_thumbnail_url()
					sarray.append({ "slug":s4.slug, "year":s4.created_at.year, "newsrooms":s4.newsrooms, "headline":s4.headline, "summary":s4.summary, "original_url":s4.original_url, "primary_image": purl, "id":s4.id })
		
		# TODO : add api audit
		p = get_object_or_404(Key, api_key=api_key)
	else:
		sarray = []

	return render_to_response('api/'+version+'/stories_by_filters_'+dif+'.html', { 'stories': sarray, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def story(request,api_key,story_id,dif='json',custom_filter='',extra_context=None,version=settings.API_VERSION):
	story = get_object_or_404(Story, pk=story_id)
	
	if custom_filter == '_ec':
		extra_context = {'awards':Award.objects.get_for_object(story)}
	#if custom_filter == '_republish':
	#	extra_context = {'plaintext':PlainText.objects.filter(story=story)}
	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/story'+custom_filter+'_'+dif+'.html', { 'story': story, 'extra_context': extra_context, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def media(request,api_key,media_id,dif='json',version=settings.API_VERSION):
	media = get_object_or_404(Media, pk=media_id)

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/media_'+dif+'.html', { 'media': media, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)

def newsrooms_categories(request,api_key,dif='json',version=settings.API_VERSION):
	newsrooms = Tag.objects.usage_for_model(Newsroom)

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/newsrooms_'+dif+'.html', { 'newsrooms': newsrooms, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)

def newsrooms_bios(request,api_key,newsroom_id,dif='json',version=settings.API_VERSION):
	n = get_object_or_404(Newsroom,pk=newsroom_id)
	bios = Profile.objects.filter(user__in=n.members.values_list('id',flat=True)).distinct().order_by('last_name')

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/newsroom_bios_'+dif+'.html', { 'bios': bios, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def bios_by_filters(request,api_key,dif='json',version=settings.API_VERSION):
	if request.method == 'POST':
		newsrooms_filter = request.POST.get("newsrooms",'').split(',')
		newsrooms = Newsroom.objects.filter(id__in=newsrooms_filter)
		
		#print newsrooms
		profiles = []
		for n in newsrooms:
			for p in n.members.values_list('id',flat=True):
				profiles.append(p)
		
		#print profiles
		bios = Profile.objects.filter(user__in=profiles).distinct().order_by('last_name')

		# TODO : add api audit
		p = get_object_or_404(Key, api_key=api_key)
	else:
		bios = []

	return render_to_response('api/'+version+'/newsroom_bios_'+dif+'.html', { 'bios': bios, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)

def organizations(request,api_key,organization_id,dif='json',version=settings.API_VERSION):
	org = get_object_or_404(NewsOrganization, pk=organization_id)
	newsrooms = Newsroom.objects.filter(organization=org).order_by('created_at')
	metastories = MetaStory.objects.filter(newsrooms__in=newsrooms.values_list('id',flat=True))
	projects = Project.objects.filter(id__in=metastories.values_list('project',flat=True)).distinct()
	profiles = Profile.objects.all()
	
	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)
	
	return render_to_response('api/'+version+'/organizations_'+dif+'.html', { 'organization': org, 'metastories': metastories, 'projects': projects, 'profiles':profiles, 'newsrooms':newsrooms, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def bio(request,api_key,user_id,dif='json',version=settings.API_VERSION):
	bio = Profile.objects.get(user_id=user_id)
	
	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/bio_'+dif+'.html', { 'bio': bio, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)


def story_placements(request,api_key,story_id,dif='json',version=settings.API_VERSION):
	story = get_object_or_404(Story, pk=story_id)
	placements = StoryPlacements.objects.filter(story=story)[5]
	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/story_placements_'+dif+'.html', { 'placements': placements, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)



##
## new in v2
##

def placements(request,api_key,mention=False,version=settings.API_VERSION):
	placements = StoryPlacements.objects.filter(is_mention=mention).order_by('-story_ran')
	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/placements.json', { 'placements': placements, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/json')

def partners_by_year(request,api_key,year_id,version=settings.API_VERSION):
	placements = StoryPlacements.objects.filter(story_ran__year=year_id,is_mention=False)
	partners = Partner.objects.filter(id__in=placements.values_list('partner',flat=True)).distinct().order_by('name')
	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/partners.json', { 'partners': partners, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/json')

def newsrooms(request,api_key,dif='json',version=settings.API_VERSION):
	newsrooms = Newsroom.objects.all().order_by('name')

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/newsrooms.json', { 'newsrooms': newsrooms, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/json')

def projects(request,api_key,version=settings.API_VERSION):
	projects = Project.objects.all().order_by('name')

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/projects.json', { 'projects': projects, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/json')

def packages(request,api_key,version=settings.API_VERSION):
	packages = MetaStory.objects.filter(is_active=1,status='Approved').order_by('headline')

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/packages.json', { 'packages': packages, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/json')

def stories(request,api_key,version=settings.API_VERSION):
	stories = Story.objects.filter(is_active=1,status='Approved').order_by('headline')

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/stories.json', { 'stories': stories, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/json')

def organization(request,api_key,organization_id,dif='json',version=settings.API_VERSION):
	org = get_object_or_404(NewsOrganization, pk=organization_id)
	newsrooms = Newsroom.objects.filter(organization=org).order_by('created_at')
	metastories = MetaStory.objects.filter(newsrooms__in=newsrooms.values_list('id',flat=True))
	projects = Project.objects.filter(id__in=metastories.values_list('project',flat=True)).distinct()
	profiles = Profile.objects.all()

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/organizations.json', { 'organization': org, 'metastories': metastories, 'projects': projects, 'profiles':profiles, 'newsrooms':newsrooms, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/'+dif)

def awards(request,api_key,version=settings.API_VERSION):
	awards = Award.objects.all()

	# TODO : add api audit
	p = get_object_or_404(Key, api_key=api_key)

	return render_to_response('api/'+version+'/awards.json', { 'awards': awards, 'callback':request.REQUEST.get('callback','') }, context_instance=RequestContext(request), mimetype='application/json')


#def project(request,api_key,project_id,dif='json',version=settings.API_VERSION):
#	metastories = MetaStory.objects.filter(project=project_id).order_by('headline')
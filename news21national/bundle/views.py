from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import get_object_or_404

from news21national.bundle.models import StoryBundle
from news21national.story.models import Story
from news21national.multimedia.models import Media

def get_bundle(request,slug):
	bundle = get_object_or_404(StoryBundle, slug=slug)
	stories = Story.objects.filter(id__in=bundle.stories.values_list('id',flat=True))
	images = Media.children.filter(id__in=stories.values_list('primary_image',flat=True),_child_name="photo",status="Approved")
	multimedia = Media.children.filter(story__in=stories.values_list('id',flat=True),status="Approved")
	return render_to_response('bundle/list.html', { 'bundle': bundle, 'stories':stories, 'images':images,'multimedia':multimedia }, context_instance=RequestContext(request))
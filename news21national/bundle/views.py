from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import get_object_or_404

from news21national.bundle.models import StoryBundle
from news21national.story.models import Story

def get_bundle(request,slug):
	bundle = get_object_or_404(StoryBundle, slug=slug)
	stories = Story.objects.filter(id__in=bundle.stories.values_list('id',flat=True))
	return render_to_response('bundle/list.html', { 'bundle': bundle, 'stories':stories }, context_instance=RequestContext(request))
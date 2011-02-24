from datetime import datetime
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
import django.contrib.auth.models as auth
from django.conf import settings
from geopy import geocoders 

from django.template import RequestContext

@login_required
def geopoint_from_address(request):
	response_dict = {}
	
	if request.method == 'POST':
		if len(request.POST.get("useraddress",'')) != 0:
			address = request.POST.get("useraddress",'')
			try:
				g = geocoders.Google(settings.GOOGLE_MAPS_API_KEY)
				(place, point) = g.geocode(address)
				response_dict.update({'success': True, 'place':place, 'point':point})
			except:
				response_dict.update({'success': False})
		else:
			response_dict.update({'success': False})
	else:
		response_dict.update({'success': False})
		
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')



def server_error_500(request, template_name='500.html'):
	"""
	500 error handler.

	Templates: `500.html`
	Context: None
	"""
	return render_to_response(template_name,{'MEDIA_URL': settings.MEDIA_URL}, context_instance=RequestContext(request))

def server_error_404(request, template_name='404.html'):
	"""
	404 error handler.

	Templates: `404.html`
	Context: None
	"""
	return render_to_response(template_name,{'MEDIA_URL': settings.MEDIA_URL}, context_instance=RequestContext(request))
from datetime import datetime
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import django.contrib.auth.models as auth
from django.conf import settings
from geopy import geocoders 

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
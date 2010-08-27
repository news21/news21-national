from datetime import datetime
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import django.contrib.auth.models as auth

from geopy import geocoders 

@login_required
def geopoint_from_address(request,address):
	response_dict = {}
	
	if request.method == 'GET':
		try:
			us = geocoders.GeocoderDotUS()
			place, (lat, lng) = us.geocode(address)
			response_dict.update({'success': True})
		except:
			response_dict.update({'success': False})
	else:
		response_dict.update({'success': False})
	
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')
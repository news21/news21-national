# -*- coding: utf-8 -*-
from django.contrib.auth.forms import *
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from news21national.story.constants import STAGE_CHOICES, STAGE_DEFAULT, STATUS_DEFAULT, STATUS_CHOICES
from news21national.story.models import MetaStory, Story
from news21national.multimedia.models import Media
from news21national.newsroom.models import Newsroom
from news21national.editorsdesk.models import EditorsDesk
from discussion.models import CommentNode

from django.core import serializers

import googleanalytics
import datetime
import unittest


def getProfileById(pid):
	for p in settings.GA_ACCOUNTS_PROFILES:
		if(pid == p['profile_id']):
			return p['profile_name']
	return pid

@login_required
def dashboard(request):
	desks = EditorsDesk.objects.filter(editors=request.user).distinct()
	newsrooms = Newsroom.objects.filter(id__in=desks.values_list('newsroom',flat=True)).distinct()
	metastories = MetaStory.objects.filter(newsrooms__in=newsrooms.values_list('id',flat=True))
	stories = Story.objects.filter(metastory__in=metastories.values_list('id',flat=True))
	pending_assets = Media.children.filter(story__in=stories.values_list('id',flat=True),status="Pending Approval")[:15]
	
	return render_to_response( "editorsdesk/dashboard.html", {'newsrooms':newsrooms,'pending_assets':pending_assets,'metastories':metastories}, context_instance=RequestContext(request))

@login_required
def review_metastory(request,metastory_id):
	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	metastory.status = request.POST.get("status",STATUS_DEFAULT)
	metastory.stage = request.POST.get("stage",STAGE_DEFAULT)
	metastory.save()
	
	if request.POST.get("comment",None) != "":
		ctype = ContentType.objects.get_for_model(metastory)
		comment = CommentNode(user=request.user,body=request.POST.get("comment",""),object_id=metastory.id,content_type=ctype)
		comment.save()

	request.user.message_set.create(message="1|MetaStory Status/Comment Saved.")
	return HttpResponseRedirect( reverse('editorsdesk_review_metastory', args=[metastory_id]) )

@login_required
def review_story(request,metastory_id,story_id):
	metastory = get_object_or_404(MetaStory, pk=metastory_id)
	story = get_object_or_404(Story, pk=story_id, metastory=metastory)
	story.status = request.POST.get("status",STATUS_DEFAULT)
	story.stage = request.POST.get("stage",STAGE_DEFAULT)
	story.save()

	if request.POST.get("comment",None) != "":
		ctype = ContentType.objects.get_for_model(story)
		comment = CommentNode(user=request.user,body=request.POST.get("comment",""),object_id=story.id,content_type=ctype)
		comment.save()

	request.user.message_set.create(message="1|Story Status/Comment Saved.")
	return HttpResponseRedirect( reverse('editorsdesk_review_story', args=[metastory_id,story_id]) )

@login_required
def review_multimedia(request,multimedia_id):
	multimedia = get_object_or_404(Media, pk=multimedia_id)
	multimedia.status = request.POST.get("status",STATUS_DEFAULT)
	multimedia.stage = request.POST.get("stage",STAGE_DEFAULT)
	multimedia.save()
	
	story = get_object_or_404(Story, pk=multimedia.story.id)
	
	if request.POST.get("comment",None) != "":
		ctype = ContentType.objects.get_for_model(multimedia)
		comment = CommentNode(user=request.user,body=request.POST.get("comment",""),object_id=multimedia.id,content_type=ctype)
		comment.save()
	
	request.user.message_set.create(message="1|Multimedia Status/Comment Saved.")
	return HttpResponseRedirect( reverse('editorsdesk_review_story', args=[story.metastory.id,story.id]) )


@login_required
def analytics(request):
	connection = googleanalytics.Connection()
	valid_profile_ids = googleanalytics.config.get_valid_profiles()
	
	ed = datetime.date.today()
	end_date = ed
	if(request.POST.get("metrics_enddate","") != ""):
		ed = request.POST.__getitem__("metrics_enddate").split('/')
		end_date = datetime.datetime(int(ed[2]),int(ed[0]),int(ed[1]))
	
	start_date = sd = (end_date - datetime.timedelta(30))
	if(request.POST.get("metrics_startdate","") != ""):
		sd = request.POST.__getitem__("metrics_startdate").split('/')	 
		start_date = datetime.datetime(int(sd[2]),int(sd[0]),int(sd[1]))
	
	mets = request.POST.getlist('metrics_metrics[]')
	dims = request.POST.getlist('metrics_dimensions[]')
	sorter = request.POST.getlist('metrics_sort')
	
	#a1 = [538,894,5507,10778,2967,3308,2717,3078]
	#a2 = [3114,5931,39448,14405,32926,14913,11125,14683]
	#a3 = [14841,10829,14288,14303,16876,14986,11483,13170]
	#a4 = [4256,5295,21697,18416,15481,12798,9819,11419]
	#'a1':a1,'a2':a2,'a3':a3,'a4':a4
	
	#{% chart %}
	#	{% chart-data a1 a2 a3 a4 %}
	#	{% chart-type "line" %}
	#	{% chart-size "800x250" %}
	#	{% chart-colors "301BDF" "00CC00" "333333" "CC0000" %}
	#	 {% chart-legend "Liberty vs. Security - 2006" "Faces of Faith in America - 2007" "What's at Stake: Election - 2008" "Changing America - 2009" %}
	#	 {% chart-grid 15 15 1 1 %}
	#	{% axis "left" %}
	#	   {% axis-range 0 40000 %}
	#	 {% endaxis %}
	#	 {% axis "bottom" %}
	#	   {% axis-labels "Jun" "Jul" "Aug" "Sept" "Oct" "Nov" "Dec" "Jan" %}
	#	 {% endaxis %}
	#{% endchart %}
	#{% chart-line-style 3 6 3 %}
	
	
	
	#print request.POST.getlist('metrics_profile[]')
	data = []
	showMetrics = False
	if(request.POST.get("metrics_generated",'0') == '1'):
		showMetrics = True
		for profile_id in valid_profile_ids:
			if(profile_id in request.POST.getlist('metrics_profile[]')):
				account = connection.get_account(profile_id)
				metrics = account.get_data(start_date, end_date, metrics=mets, dimensions=dims, sort=sorter)
			
				#print metrics
			
				if(request.POST.get("metrics_chart","") != ""):
					points = []
					point_type = str(request.POST.__getitem__("metrics_chart"))
					print point_type
					for m in metrics:
						for p in m.metrics:
							if(p.name == point_type):
								points.append(p.value)
							#points.append(m[point_type])
					pdata = {'account':getProfileById(profile_id),'metrics':metrics,'chart_data':points}
				else:
					pdata = {'account':getProfileById(profile_id),'metrics':metrics}

				data.append(pdata)
		#print "call made for profile ",str(profile_id)
		#print data
	return render_to_response( "editorsdesk/analytics.html", {'profiles_data':data,'showMetrics':showMetrics,'profiles':settings.GA_ACCOUNTS_PROFILES}, context_instance=RequestContext(request))

@login_required
def report_daterange(request):
	
	def M(d): return d.year*12 + d.month
	
	connection = googleanalytics.Connection()
	valid_profile_ids = googleanalytics.config.get_valid_profiles()

	ed = datetime.date.today()
	end_date = ed
	if(request.POST.get("metrics_enddate","") != ""):
		ed = request.POST.__getitem__("metrics_enddate").split('/')
		end_date = datetime.datetime(int(ed[2]),int(ed[0]),int(ed[1]))

	start_date = sd = (end_date - datetime.timedelta(30))
	if(request.POST.get("metrics_startdate","") != ""):
		sd = request.POST.__getitem__("metrics_startdate").split('/')	 
		start_date = datetime.datetime(int(sd[2]),int(sd[0]),int(sd[1]))

	mets = ['visitors','visits','pageviews','timeOnSite','bounces','newVisits']
	dims = ['month','year']
	sorter = ['year','month']
	totals = [0,0,0,0,0,0]
	
	datalabels = []
	for r in range( M(end_date) - M(start_date) + 1 ):
		md = int(sd[0])+r
		nm = md%12 if md < 12 else md - 12 if md > 12 else 12
		ny = int(sd[2])+(md/12) if md > 12 else int(sd[2])
		
		datalabels.append( datetime.date(ny, nm, 1).strftime("%b %y") )
	
	data = []
	for profile_id in valid_profile_ids:
		if(profile_id in request.POST.getlist('metrics_profile[]')):
			datamax = 0
			account = connection.get_account(profile_id)
			metrics = account.get_data(start_date, end_date, metrics=mets, dimensions=dims, sort=sorter)
			points = []
			
			for m in metrics:
				for p in m.metrics:
					for idx, val in enumerate(mets):
						if(p.name == val):
							totals[idx] += int(p.value) if (p.type == 'integer') else float(p.value)
					if(p.name == "visitors"):
						points.append(p.value)
						if(p.value > datamax):
							datamax = p.value
			pdata = {'account':getProfileById(profile_id),'metrics':metrics,'chart_data':points,'datamax':datamax}
			
			data.append(pdata)
	
	breadcrumb = [ {'title':'Analytics','url':reverse('editorsdesk_analytics')} ]
	return render_to_response( "editorsdesk/analytics_report_daterange.html", {'profiles_data':data,'datalabels':datalabels,'datatotals':totals,'breadcrumb':breadcrumb,'profiles':settings.GA_ACCOUNTS_PROFILES}, context_instance=RequestContext(request))

@login_required
def report_alllast30days(request):
	connection = googleanalytics.Connection()
	valid_profile_ids = googleanalytics.config.get_valid_profiles()

	end_date = datetime.date.today()
	start_date = (end_date - datetime.timedelta(30))
	
	mets = ['visitors','visits','pageviews','timeOnSite','bounces','newVisits']
	dims = ['date']
	sorter = ['date']
	totals = [0,0,0,0,0,0]

	data = []
	for profile_id in valid_profile_ids:
		account = connection.get_account(profile_id)
		metrics = account.get_data(start_date, end_date, metrics=mets, dimensions=dims, sort=sorter)
		t = [{'label':'visitors','data':0},{'label':'visits','data':0},{'label':'pageviews','data':0},{'label':'timeOnSite','data':0},{'label':'bounces','data':0},{'label':'newVisits','data':0}]
		for m in metrics:
			for p in m.metrics:				
				for idx, val in enumerate(mets):
					if(p.name == val):
						totals[idx] += int(p.value) if (p.type == 'integer') else float(p.value)
				for pt in t:
					if(pt['label'] == p.name):
						pt['data'] += int(p.value) if (p.type == 'integer') else float(p.value)
		pdata = {'account':getProfileById(profile_id),'metrics':metrics,'totals':t}
					
		data.append(pdata)
		#print pdata
	
	breadcrumb = [ {'title':'Analytics','url':reverse('editorsdesk_analytics')} ]
	return render_to_response( "editorsdesk/analytics_report_alllast30days.html", {'profiles_data':data,'datatotals':totals,'breadcrumb':breadcrumb,'profiles':settings.GA_ACCOUNTS_PROFILES}, context_instance=RequestContext(request))

@login_required
def report_firstxmonths(request):
	connection = googleanalytics.Connection()
	valid_profile_ids = googleanalytics.config.get_valid_profiles()
	
	#yesterday = datetime.timedelta(days=-1)
	#start_year = int(settings.GA_START_YEAR)
	#years = []
	#y = int(settings.GA_START_YEAR)
	#while (y < datetime.date.today().year) :
	#	 sd = datetime.date(int(y), 6, 1)
	#	 edy = y+1 if (datetime.date.today().month <= settings.GA_START_MONTH ) else y
	#	 ed = datetime.date(edy, datetime.date.today().month, 1)+yesterday
	#	 r = {'start_date':sd,'end_date':ed}
	#	 years.append(r)
	#	 y += 1
	yesterday = datetime.timedelta(days=-1)
	start_year = int(settings.GA_START_YEAR)
	years = []
	y = int(settings.GA_START_YEAR)
	while (y <= datetime.date.today().year) :
		sdm = int(settings.GA_START_MONTH)
		sdy = y
		edy = y+1 if (datetime.date.today().month <= settings.GA_START_MONTH ) else y
		edm = (datetime.date(edy, datetime.date.today().month, 1)+yesterday).month
		r = {'start_year':sdy,'start_month':sdm,'end_year':edy,'end_month':edm,'visitors':0,'visits':0,'pageviews':0}
		years.append(r)
		y += 1
	
	#print years
	
	end_date = datetime.date.today()
	start_date = datetime.date(int(settings.GA_START_YEAR), int(settings.GA_START_MONTH), 1)
	
	mets = ['visitors','visits','pageviews']
	dims = ['year','month']
	
	data = []
	for profile_id in valid_profile_ids:
		account = connection.get_account(profile_id)
		#print "using account "
		metrics = account.get_data(start_date, end_date, metrics=mets, dimensions=dims)
		#print "got metrics data"
		pydata = []
		
		# loop through the years array to totals based on defined date ranges
		for y in years:
			t = {'visitors':0,'visits':0,'pageviews':0}
			fm = []
			for m in metrics:
				rsy = y['start_year']
				rsm = y['start_month']
				rey = y['end_year']
				rem = y['end_month']
				cy = int(m.title.replace('ga:', '').split(' | ')[0].split('=')[1])
				cm = int(m.title.replace('ga:', '').split(' | ')[1].split('=')[1])
				#time.mktime(datetime.date(rsy,rsm,1).timetuple())
				
				if( datetime.date(rsy,rsm,1) <= datetime.date(cy,cm,1) and datetime.date(cy,cm,1) <= datetime.date(rey,rem,1)):
					#print str(rsm)+'-'+str(rsy)+' : '+str(cm)+'-'+str(cy)+' : '+str(rem)+'-'+str(rey)
					fm.append({'metrics':m.metrics,'title':str(cm)+'/'+str(cy)})
					# loop through the datapoint and also through totals array to calculate sum for each metric
					for p in m.metrics:
						for ptk, ptv in t.items():
							if(ptk == p.name):
								t[ptk] += int(p.value) if (p.type == 'integer') else float(p.value)

			# add profile yearly sub-total to overall totals by year
			y['visitors'] += int(t['visitors'])
			y['visits'] += int(t['visits'])
			y['pageviews'] += int(t['pageviews'])

			pymdata = {'metrics':fm,'totals':t,'range':str(rsm)+'/'+str(rsy)+' - '+str(rem)+'/'+str(rey)}
			pydata.append(pymdata)
			
		pdata = {'account':getProfileById(profile_id),'metrics':pydata}
		data.append(pdata)
	
	#print years

	breadcrumb = [ {'title':'Analytics','url':reverse('editorsdesk_analytics')} ]
	return render_to_response( "editorsdesk/analytics_report_firstxmonths.html", {'profiles_data':data,'breadcrumb':breadcrumb,'years_data':years,'profiles':settings.GA_ACCOUNTS_PROFILES}, context_instance=RequestContext(request))

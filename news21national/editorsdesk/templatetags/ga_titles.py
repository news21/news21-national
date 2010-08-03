from django import template
import datetime

register = template.Library()

def ga_title_monthyear(title):
	l = title.split(' | ')
	m = 0
	y = 0
	for t in l:
		if(t.split('=')[0] == 'ga:month'):
			m = int(t.split('=')[1])
		if(t.split('=')[0] == 'ga:year'):
			y = int(t.split('=')[1])
	#print title
	#print m
	#print y
	r = datetime.date(y, m, 1).strftime("%B %Y") if m > 0 and y > 0 else ''
	return r
	
def ga_title_date(title):
	ds = title.split('=')[1]
	y = ds[0]+''+ds[1]+''+ds[2]+''+ds[3]
	m = ds[4]+''+ds[5]
	d = ds[6]+''+ds[7]
	
	r = datetime.date(int(y), int(m), int(d)).strftime("%B %d")
	return r
	
register.simple_tag(ga_title_monthyear)
register.simple_tag(ga_title_date)
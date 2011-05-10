from django.core.management.base import BaseCommand, CommandError
from news21national.story.models import Story
from news21national.utils.nginx_rewrites import NginxRewrites

class Command(BaseCommand):
	args = ''
	help = 'Rewrites Nginx Rules Config for Approved Stories'

	def handle(self, *args, **options):
		# will need expanded on to filter by year and also seperate rewrite file by year
		rstories = Story.objects.filter(status="Approved").order_by('metastory')
		rewrites = []
		for r in rstories:
			for n in r.newsroom_shortcodes:
				if r.original_url != '':
					rewrites.append({"from":"/"+str(n)+""+str(r.id),"to":str(r.original_url)})
		#rewrites = [,{"from":"/nat456","to":"http://national.news21.com"}]
		NginxRewrites().generate_conf(rewrites)
		
		self.stdout.write('Successfully rewrote config')

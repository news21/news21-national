import sys
import os.path
from os import getcwd


class NginxRewrites:

	def generate_conf(self,rewrites):
		filename = os.path.join(getcwd(), "rewrite.conf")
		print filename
		f=open(filename,'w')
		for rule in rewrites:
			f.write('rewrite ^'+rule['from']+'$ '+rule['to']+' permanent;\n')
		f.close()
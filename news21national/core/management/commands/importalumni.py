from django.core.management.base import BaseCommand, CommandError
from example.polls.models import Poll

'''
from django.core.management import setup_environ
from datetime import date
from news21national.core.models import Profile
from news21national.newsroom.models import Newsroom
from django.contrib.auth.models import User

import sys
from news21national import settings
setup_environ(settings)
'''

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for poll_id in args:
            try:
                poll = Poll.objects.get(pk=int(poll_id))
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write('Successfully closed poll "%s"\n' % poll_id)

'''
import csv
f = open('/Users/bhalle/Desktop/geodjangodev/news21-national/news21national/alumni.csv','rU')
reader = csv.reader( f )

header_row = []

author = User.objects.get(pk=175)

for row in reader:
   if not header_row:
      header_row = row
      continue
   firstname = row[6]
   lastname = row[4]
   is_active = True
   is_superuser = False
   is_staff = False
   password = "sha1$3bcb4$bccbc87e851843bfadb73d891224b0caffb39577"
   email = row[9]

   u = User.objects.create_user(row[7],email,'news2121')
   u.save()

   newsroom_id = row[3]
   try:
      n = Newsroom.objects.get(pk=newsroom_id)
      #n.members.add(u.id)
   except:
      None

   birthdate = date(2011, 1, 1)
   expected_grad_date = date(2011, 1, 1)
   gender = "Female"
   year_in_school = 'Other'
   school = row[2]

   #Profile.objects.get_or_create(user=u, phone = '555-555-5555', gender = gender, hometown = 'Phoenix', address = '555 N. Central Ave.', address_city = 'Phoenix', address_state = 'Arizona', address_zip = '85004', birthdate = birthdate, expected_grad_date = expected_grad_date, non_edu_email = email, ethnicity = 'Other', year_in_school = 'Other', school = school, degree_area = 'Other', created_by = author, created_at = date(2011, 1, 1), updated_by = author, updated_at = date(2011, 1, 1), is_active = True, first_name = firstname, last_name = lastname)
'''
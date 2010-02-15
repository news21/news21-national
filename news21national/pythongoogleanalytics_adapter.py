# GA_CREDENTIALS_EMAIL = ''
# GA_CREDENTIALS_PSWD = ''
# GA_ACCOUNTS_PROFILES = [{'profile_name':'','profile_id':''}]

import sys
import os.path
from local_settings import *

home_directory = os.path.expanduser('~')
filename = os.path.join(home_directory, '.pythongoogleanalytics')

f=open(filename,'w')
#print "create pythongoogleanalytics config file"

f.write('[Credentials]\n')
f.write('google_account_email = '+GA_CREDENTIALS_EMAIL+' \n')
f.write('google_account_password = '+GA_CREDENTIALS_PSWD+' \n \n')

f.write('[Accounts]\n')

profile_list = ''
for p in GA_ACCOUNTS_PROFILES:
    profile_list = profile_list+" "+p['profile_id']

f.write('test_profile_ids = '+profile_list)

f.close()
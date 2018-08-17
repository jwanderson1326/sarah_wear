'''DB Configuration Settings'''

import os

HOST = 'localhost'
USER = 'root'
DB = 'weather'
PASSWD = ''

#CSV Locations

PATH_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
PATH_CSV = os.path.join(PATH_ROOT,'csv')


import os
import sys
from django.conf import settings


engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}

#
def config():
    engine = 'django.db.backends.mysql'
    name = 'db'
    hostname = 'mysql-mtrivia.openshift.dsc.umich.edu'
    if sys.platform != 'win32':
        return {
            'ENGINE': engine,
            'NAME': name,
            'USER': 'admin',
            'PASSWORD': 'admin',
            'HOST': hostname,
            'PORT': 3306,
        }
    return {
        'ENGINE': engine,
        'NAME': name,
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
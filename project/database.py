import os
import sys
from django.conf import settings


engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}

def config():
    if sys.platform != 'win32':
        return {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db',
            'USER': 'admin',
            'PASSWORD': 'admin',
            'HOST': 'mysql',
            'PORT': 3306,
        }
    return {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
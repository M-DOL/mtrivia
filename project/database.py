import os

from django.conf import settings


engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}


def config():
    engine = 'django.db.backends.mysql'
    name = 'db'
    return {
        'ENGINE': engine,
        'NAME': name,
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'mysql',
        'PORT': 3306,
    }

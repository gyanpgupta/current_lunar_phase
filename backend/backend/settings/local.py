from .defaults import *
DEBUG = True
SECRET_KEY='django-insecure-5r38df&gz*tg_vnc(u*in*nj+*0omn)eg=5#il*7@+q67onm2)'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'local_project',
        'USER': 'local_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

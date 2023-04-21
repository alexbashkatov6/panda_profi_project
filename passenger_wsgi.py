# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2028490/data/www/alexcoolon.ru/panda_profi_project')
sys.path.insert(1, '/var/www/u2028490/data/djangoenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'panda_profi_project.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

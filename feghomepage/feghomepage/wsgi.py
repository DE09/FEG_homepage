import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('/home/oem/feghomepage/')
# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/oem/feghomepage/fegvenv/lib/python3.8/site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feghomepage.settings')

application = get_wsgi_application()
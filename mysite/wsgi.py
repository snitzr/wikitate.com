# HEROKU PRODUCTION

"""
WSGI config for mystite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

"""
# comment out so this original is not dup of Heroku
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""


# """
#### begin heroku setup
from django.core.wsgi import get_wsgi_application

from dj_static import Cling

application = Cling(get_wsgi_application())

# static files start
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
# static files end

#### end heroku setup
# """

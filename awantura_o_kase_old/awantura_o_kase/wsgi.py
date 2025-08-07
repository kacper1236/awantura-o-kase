"""
WSGI config for awantura_o_kase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os, subprocess

from django.core.wsgi import get_wsgi_application

#subprocess.run(["start", "cmd", "\c", "npm run dev"], cwd = os.path.join(os.getcwd(), "../stream_overlay"), shell=True)

proc = subprocess.Popen(["cmd", "/c", "start", "cmd", "/k", "npm run dev"], cwd=os.path.join(os.getcwd(), "../stream_overlay"), shell=True)

stdout, stderr = proc.communicate()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awantura_o_kase.settings')

application = get_wsgi_application()



import os

from livereload import Server
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paycheck_to_paycheck.settings')

application = get_wsgi_application()

server = Server(application)
server.watch(
    'path_to_watch/**/*.py')
server.serve(port=8001)
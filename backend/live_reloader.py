import os

from livereload import Server
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paycheck_to_paycheck.settings')

application = get_wsgi_application()

server = Server(application)
server.watch(
    'path_to_watch/**/*.py')  # Add paths you want to watch, e.g., templates, static files
server.serve(port=8001)
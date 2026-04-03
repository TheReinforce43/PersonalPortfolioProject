import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

try:
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
except Exception as e:
    # Show exact error on every request
    def app(environ, start_response):
        error = traceback.format_exc()
        start_response('500 Internal Server Error', [
            ('Content-Type', 'text/plain'),
        ])
        return [f"Django startup error:\n{error}".encode()]
import os
import importlib
import urllib.parse
from core import Request, Response

from router import NotFound

def application(environ, start_response):
    module = os.environ['FRAMEWORK']
    module = importlib.import_module(module)
    router = getattr(module, 'routes')

    try:
        request = Request(environ)
        callback, args = router.match(request.path)
        response = callback(request, *args)
    except NotFound:
        response = Response("<h3>404 Error, Page Not found</h3>", status=404)

    start_response(response.status, response.headers.items())
    return iter(response)


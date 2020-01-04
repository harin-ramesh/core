from core import Response
from core.router import Router
from core.template import render

def hello(request, name=None):
	return render('index.html', {})

routes = Router()
routes.add_route(r'/$', hello)


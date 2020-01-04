from core import Response
from core.router import Router
from core.template import render

def hello(request, name):
	return render('index.html', {'titile':'Core','msg':'Hello'})

routes = Router()
routes.add_route(r'/hello/(.*)/$', hello)


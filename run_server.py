from wsgiref.simple_server import make_server, demo_app
from wsgi import application
import os

if __name__ == '__main__':
	print("Development server started running....")
	print("Visit:http://localhost:5000/")
	os.environ["FRAMEWORK"] = "view"
	with make_server('',5000,application) as server:
		server.serve_forever()

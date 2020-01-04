from wsgiref.simple_server import make_server, demo_app
from wsgi import application
import os
from pathlib import Path


if __name__ == '__main__':
    print("Development server started running....")
    print("Visit:http://localhost:5000/")
    os.environ['SETTINGS_MODULE'] = 'settings'
    os.environ["FRAMEWORK"] = "view"
    os.environ["PATH"] = str(Path(__file__).parent.absolute())
    with make_server('',5000,application) as server:
        server.serve_forever()



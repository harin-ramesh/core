import os
from core.wsgi import get_application

os.environ.setdefault('SETTINGS_MODULE', 'settings')
application = get_application

import os

from jinja2 import Environment, FileSystemLoader
from core import Response

from core.config import settings

def render(file_name, context):
    path = "{}/{}".format(os.environ['PATH'],settings.TEMPLATES)
    file_loader = FileSystemLoader(path)
    env = Environment(loader=file_loader)
    template = env.get_template(file_name)
    output = template.render(context)
    return Response(output)



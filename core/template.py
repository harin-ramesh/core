import os

from jinja2 import Environment, FileSystemLoader
from core import Response

def render(file_name, context):
    print(os.environ['path'])
    path = f"{os.environ['path']}/templates"
    file_loader = FileSystemLoader(path)
    env = Environment(loader=file_loader)
    template = env.get_template(file_name)
    output = template.render(context)
    return Response(output)


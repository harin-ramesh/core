import re

class NotFound(Exception):
    pass

class Router:
    def __init__(self):
        self.routing_table = []

    def add_route(self, pattern, callback):
        self.routing_table.append((pattern, callback))

    def match(self, path):
        for (pattern, callback) in self.routing_table:
            m = re.match(pattern, path)
            if m:
                return (callback, m.groups())
        raise NotFound()

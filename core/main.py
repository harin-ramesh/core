from wsgiref.headers import Headers
import http.client
import urllib.parse

class Request:
    def __init__(self, environ):
        self.environ = environ

    @property
    def args(self):
        get_args = urllib.parse.parse_qs(self.environ['QUERY_STRING'])
        return {k:v[0] for k, v in get_args.items()}

    @property
    def path(self):
        return self.environ['PATH_INFO']

class Response:
    def __init__(self, response=None, status=200, charset='utf-8', content_type='text/html'):
        self.response = [] if response is None else response
        self.charset = charset
        self.headers = Headers()
        self.headers.add_header('content-type', f'{content_type}; charset={charset}')
        self._status = status

    @property
    def status(self):
        status_string = http.client.responses.get(self._status, 'UNKNOWN STATUS')
        return f'{self._status} {status_string}'

    def __iter__(self):
        for k in self.response:
            if isinstance(k, bytes):
                yield k
            else:
                yield k.encode(self.charset)
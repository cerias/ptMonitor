__author__ = 'cerias'

from bottle import Bottle, get, run, ServerAdapter

# copied from bottle. Only changes are to import ssl and wrap the socket
class SSLWSGIRefServer(ServerAdapter):
    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        import ssl
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        srv = make_server(self.host, self.port, handler, **self.options)
        srv.socket = ssl.wrap_socket (
        	srv.socket,
        	certfile='ssl/server.pem',  # path to certificate
        	server_side=True)
        srv.serve_forever()

class WebServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()

    def _route(self):
        self._app.route('/', method='GET', callback=self._index)

    def _start(self):
        srv = SSLWSGIRefServer(host=self._host, port=self._port)
        self._app.run(server=srv)

    def _index(self):
        return 'Welcome'


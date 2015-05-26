#!/usr/bin/python

import os, threading
import SimpleHTTPServer
import SocketServer


class cfworker(threading.Thread):
        def __init__(self, port=None):
                threading.Thread.__init__(self)
		if not port:
			port = int( os.getenv("VCAP_APP_PORT") )
                self.port = port
		self.start()

        def run(self):
                Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
                httpd = SocketServer.TCPServer(("", self.port), Handler)
                print "cfworker: serving at port: %s" % self.port
                httpd.serve_forever()


cfworker()

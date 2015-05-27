#!/usr/bin/python
import flask
import threading


class cfworker(threading.Thread, flask.Flask):

        def __init__(self, port=None):
                threading.Thread.__init__(self)
                self.app = flask.Flask(__name__)
                self.port = port
                self.start()

        def run(self):
                self.app.run( host='0.0.0.0', port=self.port )

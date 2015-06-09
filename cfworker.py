#!/usr/bin/python
import flask
import multiprocessing


class cfworker(multiprocessing.Process, flask.Flask):

        def __init__(self, port=None):
                self.server = multiprocessing.Process(target=self.run)
                self.app = flask.Flask(__name__)
                self.port = port
                self.start()

        def run(self):
                self.app.run( host='0.0.0.0', port=self.port )

        def start(self):
                self.server.start()

        def stop(self):
                self.server.terminate()
                self.server.join()

#!/usr/bin/python
import flask
import multiprocessing


class cfworker(multiprocessing.Process, flask.Flask):

        def __init__(self, port=None):
                self.app = flask.Flask(__name__)
                self.port = port

        def run(self):
                self.app.run( host='0.0.0.0', port=self.port )

        def start(self):
                self.stop()
                self.server = multiprocessing.Process(target=self.run)
                try:
                        self.server.start()
                except AssertionError as e:
                        pass

        def stop(self):
                try:
                        self.server.terminate()
                        self.server.join()
                except AttributeError as e:
                        pass

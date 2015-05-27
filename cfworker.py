#!/usr/bin/python
import os
from flask import Flask
import threading
import logging

app = Flask(__name__)

class cfworker(threading.Thread):
        def __init__(self, port=None, log=None):
                threading.Thread.__init__(self)
		self.port = port
		self.log = log
		if not self.port:
			# update to default CF port
			self.port = int(os.getenv("VCAP_APP_PORT"))
		if self.log:
			# update from the system default
			logging.getLogger('werkzeug').setLevel(self.log)
		self.start()
               	app.run( host='0.0.0.0', port=self.port )

        def run(self):
                # implement this function in your own app    
                pass

@app.route('/')
def index():
	""" Routes are optional """
        return "Hello cfworker!"


#!/usr/bin/python
import os
from flask import Flask
import threading

class cfworker(threading.Thread):
        def __init__(self, port=None):
                threading.Thread.__init__(self)
                self.start()
		self.port = port
       	        self.app = Flask(__name__)
               	self.app.run( host='0.0.0.0', port=self.port )

        def run(self):
                self.work()

        def work(self):
                # implement this function in your own app    
                pass

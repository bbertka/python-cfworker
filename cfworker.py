#!/usr/bin/python
import os
from flask import Flask
import threading

class cfworker(threading.Thread):
        def __init__(self, port):
                threading.Thread.__init__(self)
                self.start()
       	        self.app = Flask(__name__)
               	self.app.run( host='0.0.0.0', port=port )

        def run(self):
                self.work()

        def work(self):
                # implement this function in your own app    
                pass

#!/usr/bin/python
import os
from flask import Flask
import threading

app = Flask(__name__)

class cfworker(threading.Thread):
        def __init__(self, port=None):
                threading.Thread.__init__(self)
                self.start()
		self.port = port
               	app.run( host='0.0.0.0', port=self.port )

        def run(self):
                self.work()

        def work(self):
                # implement this function in your own app    
                pass

@app.route('/')
def index():
        return "Welcome to cfworker"


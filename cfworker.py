#!/usr/bin/python
import os
from flask import Flask
import threading

class CFworker(threading.Thread):
        def __init__(self):
                threading.Thread.__init__(self)
                self.start()
                self.port = int( os.getenv("VCAP_APP_PORT") )
                self.app = Flask(__name__)
                self.app.run( host='0.0.0.0', port=self.port )

        def run(self):
                self.work()

        def work(self):
                # implement this function in your own app    
                pass

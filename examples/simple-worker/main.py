#!/usr/bin/python
import cfworker
import time

worker = cfworker.cfworker( port=int(os.getenv('VCAP_APP_PORT')) )
worker.start()

while True:
	print 'working...'
	time.sleep(5)

worker.stop()


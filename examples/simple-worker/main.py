#!/usr/bin/python
import cfworker
import time

worker = cfworker.cfworker()
worker.start()

while True:
	print 'working...'
	time.sleep(5)

worker.stop()


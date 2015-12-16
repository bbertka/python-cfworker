#!/usr/bin/python
import cfworker
import time, os

worker = cfworker.cfworker()
worker.start()

while True:
	print 'working...'
	time.sleep(2)

worker.stop()


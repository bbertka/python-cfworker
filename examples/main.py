#!/usr/bin/python
import cfworker
import time


cfworker.cfworker()

while True:
	print 'working...'
	time.sleep(5)



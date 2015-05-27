#!/usr/bin/python

import cfworker
import time

class cfworker(cfworker.cfworker):
	""" cfworker.work must be overridden as shown here """

	def work(self):
		while True:
                	print "cfworker: Working..."
			time.sleep(5)


if __name__=='__main__':

	w = cfworker()

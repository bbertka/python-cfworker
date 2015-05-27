#!/usr/bin/python

import cfworker


class cfworker(cfworker.cfworker):
	""" cfworker.work must be overridden as shown here """

	def work(self):
		while True:
                	print "cfworker: Working..."


if __name__=='__main__':

	w = cfworker()

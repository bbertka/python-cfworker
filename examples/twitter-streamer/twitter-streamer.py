#!/usr/bin/python
import os
import cfworker
from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code


if __name__=='__main__':

	""" Leave this as is if deploying to CF, otherwise choose
	a port for local deployment (e.g. 8080) """

	worker = cfworker.cfworker( port=int(os.getenv('VCAP_APP_PORT')) )

	""" These variables can be set in your environment (ideal), or
	hardcoded into the function call """

	stream = MyStreamer(os.getenv('APP_KEY'), os.getenv('APP_SECRET'),
                    os.getenv('OAUTH_TOKEN'), os.getenv('OAUTH_TOKEN_SECRET') )

	""" You can also set an environment variable to choose what to track, or 
	hard code a list here """
	stream.statuses.filter(track='bigdata')

	""" stops the HTTP server """
	worker.stop()

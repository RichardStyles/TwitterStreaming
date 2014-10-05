# -*- coding: utf-8 -*-
'''
	Save Twitter Streaming API to a compressed CSV.GZ file 

	author:: Richard Styles
'''
import sys
sys.path.insert(0,'./twitter');
sys.path.insert(0,'./unicodecsv');
from twython import TwythonStreamer
import collections
import unicodecsv as csv
from config import *
import datetime
import os.path
import gzip

# pre-list known optional keys which are not included in all Stream responses. - ensures CSV integrity
allkeys = ['coordinates','geo','entities_media','extended_entities_media','place_attributes_street_address','entities_trends','coordinates_coordinates','coordinates_type','geo_type','geo_coordinates','user_profile_banner_url']

# set initial count for processed tweets
tcount = 0

def flatten(d, parent_key='', sep='_'):
	'''	take multi-dimension dictionary flatten and rename keys accordingly.

		Args:
			d (dict) : multi dimension dictionary 
	'''
	items = []
	for k, v in d.items():
		new_key = parent_key + sep + k if parent_key else k
		if v and isinstance(v, collections.MutableMapping):
			items.extend(flatten(v, new_key).items())
		else:
			items.append((new_key, v))
	return dict(items)
def checkOptKeys(d):
	global tcount
	'''	Check flattened array for any 'extra' keys in response.

		if `** new key found:` prints then key needs to be added to allkeys list
		on first response standard keys are added.

		if key does not exist on response then default to empty string.
	'''
	for key, value in d.iteritems():
		if key not in allkeys:
			if tcount > 0:
				print "** new key found - update required: " + key
			allkeys.append(key)
	for k in allkeys:
		if not d.has_key(k):
			d[k] = ''
	return d
def tweetCounter():
    global tcount
    # increment tcount
    tcount += 1
    # output infomation to console
    sys.stdout.write('\rtweet %d recorded' % tcount)
    sys.stdout.flush()
    return

class StreamToCSV(TwythonStreamer):

	def on_success(self, data):
		global tcount
		global allkeys
		# Flatten data
		dd = flatten(data)
		dd = checkOptKeys(dd)
		# order keys to maintain csv integrity
		dd = collections.OrderedDict(sorted(dd.items()))

		# get keys for csv writer
		rowData = dd.values()
		rowHeader = dd.keys()

		# get current date and hour
		now = datetime.datetime.now()
		
		# create filename based on date and hour
		f = 'streamdata/data-'+now.strftime("%Y-%m-%d-%H")
		
		# does this file already exisit ?
		addHeader = os.path.isfile('%s.csv.gz' % f)

		# open csv file or create to write to
		with gzip.open('%s.csv.gz' % f, 'a') as csvfile:
			twitterbuffer = csv.writer(csvfile,allkeys)
			# is this a new file? if so add headers
			if(addHeader == False):
				twitterbuffer.writerow(rowHeader)
			# write data row
			twitterbuffer.writerow(rowData)

			# increment twitter counter on console display
			tweetCounter()

			# ensure file close 
			csvfile.close()

	def on_error(self, status_code, data):
		# default error output from tywthonstreamer 
		# TODO: improve ?
		print status_code, data

# Requires Authentication as of Twitter API v1.1
stream = StreamToCSV(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	print "*****  Twitter Streaming API  *****"
	print "  Press ctrl + c to exit"


	print "Listing current parameters"
	for k,v in STREAM_PARAMS.iteritems():
		if isinstance(v, basestring):
			print '  %7s : %s' % (k,v)
		elif isinstance(v, ( int, long )):
			print '  %7s : %s' % (k,str(v))
		elif isinstance(v, (list, dict)):
			print '  %7s : %s' % (k,str(v).strip('[]'))
	print "Start Stream:"
	stream.statuses.filter(**STREAM_PARAMS)

#	Catch ctrl+c exit from command line
except (KeyboardInterrupt, SystemExit):
	print "\n*****       End program       *****"
	sys.exit(0)

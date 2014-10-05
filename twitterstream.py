# -*- coding: utf-8 -*-
import sys
#import csv
sys.path.insert(0,'./twitter');
sys.path.insert(0,'./unicodecsv');
from twython import TwythonStreamer
import collections
import unicodecsv as csv
from config import *
import datetime
import os.path
import gzip

#allkeys = ['user_profile_banner_url','user_location','possibly_sensitive','coordinates_coordinates','coordinates','geo','entities_media','extended_entities_media']
allkeys = ['coordinates','geo','entities_media','extended_entities_media','place_attributes_street_address','entities_trends','coordinates_coordinates','coordinates_type','geo_type','geo_coordinates','user_profile_banner_url']
tcount = 0
def flatten(d, parent_key='', sep='_'):
	items = []
	for k, v in d.items():
		new_key = parent_key + sep + k if parent_key else k
		if v and isinstance(v, collections.MutableMapping):
			items.extend(flatten(v, new_key).items())
		else:
			items.append((new_key, v))
	return dict(items)
def checkOptKeys(d):
	for key, value in d.iteritems():
		if key not in allkeys:
			print "** new key found: " + key
			allkeys.append(key)
	for k in allkeys:
		if not d.has_key(k):
			d[k] = ''
	return d
def tweetCounter():
    global tcount
    tcount += 1
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

		rowData = dd.values()
		rowHeader = dd.keys()
		# set None values to empty string
		#rowData = ['' if v is None else v for v in row]
		# get current date and hour
		now = datetime.datetime.now()
		# create filename based on date and hour
		f = 'streamdata/data-'+now.strftime("%Y-%m-%d-%H")
		# does this file already exisit ?
		addHeader = os.path.isfile('%s.csv.gz' % f)
		# open csv file or create to write to
		#print allkeys
		with gzip.open('%s.csv.gz' % f, 'a') as csvfile:
			twitterbuffer = csv.writer(csvfile,allkeys)
			#if(addHeader == False):
			twitterbuffer.writerow(rowHeader)
			twitterbuffer.writerow(rowData)
			tcount += 1
			tweetCounter()
			csvfile.close()

	def on_error(self, status_code, data):
		print status_code, data

# Requires Authentication as of Twitter API v1.1
stream = StreamToCSV(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	print "*****  Twitter Streaming API  *****"
	stream.statuses.filter(language='en',locations=[-0.489,51.28,0.236,51.686])
except (KeyboardInterrupt, SystemExit):
	print "\n*****       End program       *****"
	sys.exit(0)

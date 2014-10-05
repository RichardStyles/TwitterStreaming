# -*- coding: utf-8 -*-
import sys
#import csv
sys.path.insert(0,'./twitter');
sys.path.insert(0,'./unicodecsv');
from twython import TwythonStreamer
import unicodecsv as csv
from config import *
import datetime
import os.path


class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		#print data
		
		dataArr = [data['contributors'],data['truncated'],data['text'],data['in_reply_to_status_id'],data['id'],data['favorite_count'],data['source'],data['retweeted'],data['coordinates'],data['timestamp_ms'],data['entities'],data['entities']['user_mentions'],data['entities']['symbols'],data['entities']['trends'],data['entities']['hashtags'],data['entities']['urls'],data['in_reply_to_screen_name'],data['id_str'],data['retweet_count'],data['in_reply_to_user_id'],data['favorited'],data['user'],data['user']['follow_request_sent'],data['user']['profile_use_background_image'],data['user']['default_profile_image'],data['user']['id'],data['user']['verified'],data['user']['profile_image_url_https'],data['user']['profile_sidebar_fill_color'],data['user']['profile_text_color'],data['user']['followers_count'],data['user']['profile_sidebar_border_color'],data['user']['id_str'],data['user']['profile_background_color'],data['user']['listed_count'],data['user']['profile_background_image_url_https'],data['user']['utc_offset'],data['user']['statuses_count'],data['user']['description'],data['user']['friends_count'],data['user']['location'],data['user']['profile_link_color'],data['user']['profile_image_url'],data['user']['following'],data['user']['geo_enabled'],data['user']['profile_background_image_url'],data['user']['name'],data['user']['lang'],data['user']['profile_background_tile'],data['user']['favourites_count'],data['user']['screen_name'],data['user']['notifications'],data['user']['url'],data['user']['created_at'],data['user']['contributors_enabled'],data['user']['time_zone'],data['user']['protected'],data['user']['default_profile'],data['user']['is_translator'],data['geo'],data['in_reply_to_user_id_str'],data['possibly_sensitive'],data['lang'],data['created_at'],data['filter_level'],data['in_reply_to_status_id_str'],data['place'],data['place']['full_name'],data['place'],data['place']['url'],data['place']['country'],data['place']['place_type'],data['place']['bounding_box'],data['place']['bounding_box']['type'],data['place']['bounding_box']['coordinates'],data['place']['country_code'],data['place']['attributes'],data['id']]
		now = datetime.datetime.now()
		f = 'streamdata/data-'+now.strftime("%Y-%m-%d-%H")

		addHeader = os.path.isfile('%s.csv' % f)
		with open('%s.csv' % f, 'a') as csvfile:
			twitterbuffer = csv.writer(csvfile, dialect='excel')
			if(addHeader == False):
				twitterbuffer.writerow(['contributors','truncated','text','in_reply_to_status_id','id','favorite_count','source','retweeted','coordinates','timestamp_ms','entities','entities-user_mentions','entities-symbols','entities-trends','entities-hashtags','entities-urls','in_reply_to_screen_name','id_str','retweet_count','in_reply_to_user_id','favorited','user','user-follow_request_sent','user-profile_use_background_image','user-default_profile_image','user-id','user-verified','user-profile_image_url_https','user-profile_sidebar_fill_color','user-profile_text_color','user-followers_count','user-profile_sidebar_border_color','user-id_str','user-profile_background_color','user-listed_count','user-profile_background_image_url_https','user-utc_offset','user-statuses_count','user-description','user-friends_count','user-location','user-profile_link_color','user-profile_image_url','user-following','user-geo_enabled','user-profile_banner_url','user-profile_background_image_url','user-name','user-lang','user-profile_background_tile','user-favourites_count','user-screen_name','user-notifications','user-url','user-created_at','user-contributors_enabled','user-time_zone','user-protected','user-default_profile','user-is_translator','geo','in_reply_to_user_id_str','possibly_sensitive','lang','created_at','filter_level','in_reply_to_status_id_str','place','place-full_name','place','place-url','place-country','place-place_type','place-bounding_box','place-bounding_box-type','place-bounding_box-coordinates','place-country_code','place-attributes','id','name'])
			twitterbuffer.writerow(dataArr)
			print 'tweet recorded'
			csvfile.close()
    	#print data
        #if 'text' in data:
        #    print data['text'].encode('utf-8')
        # Want to disconnect after the first result?
        # self.disconnect()

	def on_error(self, status_code, data):
		print status_code, data

# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#stream.statuses.filter(track='twitter')
stream.statuses.filter(language='en',locations=[-0.489,51.28,0.236,51.686])
# stream.user()
# Read the authenticated users home timeline
# (what they see on Twitter) in real-time
# stream.site(follow='twitter')

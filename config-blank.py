'''
	Set Twitter API OAuth Keys, Token & Secret
 
'''
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
'''
	Set Twitter Streaming API parameters
 ----------------------------------------------
		For all parameters please go to https://dev.twitter.com/streaming/overview/request-parameters

 		language='en'
			request english only tweets

		locations=[-0.489,51.28,0.236,51.686]
			get tweets posted from specific location (example given is London, UK)

'''
STREAM_PARAMS = {'language':'en','locations':[-0.489,51.28,0.236,51.686]}
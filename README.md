Python Twitter Streaming
================
Python Application to use Twitter's streaming API to save tweet data to a compressed csv.gz format.
Developed in Python version 2.7.7

###About

This application was written to help people gain access to the Twitter Streaming API. The Streaming API allows for much greater access to twitter tweets.

New csv.gz files will be added to the streamdata folder (gitignore'd by default)

Files are created every hour in the following format data-YEAR-MONTH-DAY-HOUR.csv.gz this is to allow post-processing of this data stream.
As Twitter's API Documents advise buffering data from the stream before processing.

###Requirements

Configobj. This is used to import user editable configuration.


```
pip install configobj
```

###Submodules

This project uses two other Python projects on GitHub:

* [twython](https://github.com/ryanmcgrath/twython)
* [Python Unicodecsv](https://github.com/jdunck/python-unicodecsv)


These currently do not need to be installed via pip as the twitterstream.py application will import from the submodules. Provided the submodules are initialised.Submodule requirements, do need to be installed. See below.

```
pip install requests
pip install requests_oauthlib
```

Twitter OAuth tokens &amp; application keys are required to be added to config.py.
Get keys from [dev.twitter.com](https://dev.twitter.com/oauth/overview/application-owner-access-tokens)
Place keys in config-blank.py and rename/copy to config.py.

###Configuration
All user configurations are defined in config.ini (see config-blank.ini). Currently required:

* Twitter API App Key
* Twitter API App Secret
* Twitter API OAuth Token
* Twitter API OAuth Token Secret
* Twitter Streaming API Parameters. Example supplied is English only tweet, posted from London (bound box)

Full list of Twitter Streaming API parameters available [here](https://dev.twitter.com/streaming/overview/request-parameters).
For help creating bounding box coordinates, try [here](http://boundingbox.klokantech.com/) and select CSV from the copy &amp; paste option.

###Example config.ini
Below is an example (without comments) of a config.ini for twitterstream application.

```
APP_KEY = 'secretkey'
APP_SECRET = 'secretkey'
OAUTH_TOKEN = 'secretkey'
OAUTH_TOKEN_SECRET = 'secretkey'
FOLDER = 'streamdata/'
FILE_NAME = 'data-'
FILE_DATETIME = "%Y-%m-%d-%H"
[STREAM_PARAMS] 	# do not change this line
language='en'
locations= -0.489,51.28,0.236,51.686
```

###Config.ini detail
Additional option to se File location and file name parameters

* FOLDER must already exist.
* FILE_NAME is a prefix for the output file.
* FILE_DATETIME is what sepearate the data based on date/time using the format:

`%Y` Year
`%m` Month
`%d` Day
`%H` Hour
`%M` Minute
`%S` Second


######For more date & time options [see](https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior)

Streaming API parameters must be in the following format:

```
[STREAM_PARAMS]		# do not change this line
parameter_name ='parameter_value'
parameter_required_array = value_1,value_2,value_3,value4
```

###Run Application

```
python twitterstream.py
```

![Bash Example](https://www.dropbox.com/s/msx1au6i3i66jlj/Screenshot%202014-10-05%2021.20.40.png?dl=1 "Bash example")

###Testing
This project is currently being tested, by recording several thousand of tweets. This is to make sure that every possible result from Twitter's Streaming API can be recorded.

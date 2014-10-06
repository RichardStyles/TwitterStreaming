Python Twitter Streaming
================
<p>Python Application to use Twitter's streaming API to save tweet data to a compressed csv.gz format.</p>
<p>Developed in Python version 2.7.7</p>

<h4>About</h4>
<p>This application was written to help people gain access to the Twitter Streaming API. The Streaming API allows for much greater access to twitter tweets.</p>
<p>New csv.gz files will be added to the streamdata folder (gitignore'd by default)<br />
Files are created every hour in the following format data-YEAR-MONTH-DAY-HOUR.csv.gz this is to allow post-processing of this data stream.<br />As Twitter's API Documents advise buffering data from the stream before processing.</p>

<h3>Requirements</h3>

<p>Configobj. This is used to import user editable configuration.</p>
```
pip install configobj
```
<h4>Submodules</h4>
This project uses two other Python projects on GitHub:
<ul>
<li><a href='https://github.com/ryanmcgrath/twython'>twython</a></li>
<li><a href='https://github.com/jdunck/python-unicodecsv'>Python Unicodecsv</a></li>
</ul>

<p>These currently do not need to be installed via pip as the twitterstream.py application will import from the submodules. Provided the submodules are initialised.</p>
<p>Submodule requirements, do need to be installed. See below.</p>

```
pip install requests
pip install requests_oauthlib
```

Twitter OAuth tokens &amp; application keys are required to be added to config.py.
Get keys from <a href='https://dev.twitter.com/oauth/overview/application-owner-access-tokens'>dev.twitter.com</a>
Place keys in config-blank.py and rename/copy to config.py.

<h3>Configuration</h3>
<p>All user configurations are defined in config.ini (see config-blank.ini). Currently required:</p>
<ul>
	<li>Twitter API App Key</li>
	<li>Twitter API App Secret</li>
	<li>Twitter API OAuth Token</li>
	<li>Twitter API OAuth Token Secret</li>
	<li>Twitter Streaming API Parameters<br>Example supplied is English only tweet, posted from London (bound box)</li>
</ul>
<p>Full list of Twitter Streaming API parameters avaliable <a href='https://dev.twitter.com/streaming/overview/request-parameters'>here</a>.<br />
For help creating bounding box coordinates, try <a href='http://boundingbox.klokantech.com/'>here</a> and select CSV from the copy &amp; paste option.<br />
Streaming API parameters must be in the following format:</p>

```
[STREAM_PARAMS]		# do not change this line

parameter_name ='parameter_value'
parameter_required_array = value_1,value_2,value_3,value4

```
<h4>Example config.ini</h4>
<p>Below is an example (without comments) of a config.ini for twitterstream application.</p>
```
APP_KEY = 'secretkey'
APP_SECRET = 'secretkey'
OAUTH_TOKEN = 'secretkey'
OAUTH_TOKEN_SECRET = 'secretkey'

[STREAM_PARAMS] 	# do not change this line
language='en'
locations= -0.489,51.28,0.236,51.686
```
<h3>Run Application</h3>
```
python twitterstream.py
```
![Bash Example](https://www.dropbox.com/s/msx1au6i3i66jlj/Screenshot%202014-10-05%2021.20.40.png?dl=1 "Bash example")

<h3>Testing</h3>
<p>This project is currently being tested, by recording several thousand of tweets. This is to make sure that every possible result from Twitter's Streaming API can be recorded.</p>

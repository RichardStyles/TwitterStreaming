Python Twitter Streaming
================
<p>Python Application to use Twitter's streaming API to save tweet data to a compressed csv.gz format.</p>

<p>Developed in Python version 2.7.7</p>

<p>New CSV.GZ files will be added to the streamdata folder (gitignore'd by default)<br />
Files are created every hour in the following format data-YEAR-MONTH-DAY-HOUR.csv.gz this is to allow post-processing of this data stream.<br />As Twitter's API Documents advise buffering data from the stream before processing.</p>

<h3>Submodules</h3>
This project uses two other git repos
<ul>
<li><a href='https://github.com/ryanmcgrath/twython'>twython</a></li>
<li><a href='https://github.com/jdunck/python-unicodecsv'>Python Unicodecsv</a></li>
</ul>

<p>These currently do not need to be installed via pip as the twitterstream.py application will import from the submodules. Provided the submodules are initialised.<br />
Submodule requirements do need to be installed, see below.</p>

```
pip install requests
pip install requests_oauthlib
```

Twitter OAuth tokens &amp; application keys are required to be added to config.py.
Get keys from <a href='https://dev.twitter.com/oauth/overview/application-owner-access-tokens'>dev.twitter.com</a>
Place keys in config-blank.py and rename/copy to config.py.

<h3>Configuration</h3>
<p>All user configurations are defined in config.py (see config-blank.py). Currently required:</p>
<ul>
	<li>Twitter API App Key</li>
	<li>Twitter API App Secret</li>
	<li>Twitter API OAuth Token</li>
	<li>Twitter API OAuth Token Secret</li>
	<li><p>Twitter Streaming API Parameters<br>Example supplied is English only tweet, posted from London (bound box)</p></li>
</ul>
<p>Streaming API parameters must be in the following format:</p>
```
STREAM_PARAMS = {'parameter_name':'parameter_value','parameter_required_array':[value_1,value_2,value_3,value4]}
```
<h4>Example config.py</h4>
<p>Below is an example (without comments) of a config.py for twitterstream application.
```
APP_KEY = 'thisisasecret'
APP_SECRET = 'thisisasecret'
OAUTH_TOKEN = 'thisisasecret'
OAUTH_TOKEN_SECRET = 'thisisasecret'
STREAM_PARAMS = {'language':'en','locations':[-0.489,51.28,0.236,51.686]}
```
<h3>Run Application</h3>
```
python twitterstream.py
```
![Bash Example](https://www.dropbox.com/s/msx1au6i3i66jlj/Screenshot%202014-10-05%2021.20.40.png?dl=1 "Bash example")

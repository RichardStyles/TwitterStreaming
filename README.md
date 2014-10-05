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

Twitter OAuth tokens & application keys are required to be added to config.py.
Get keys from <a href='https://dev.twitter.com/oauth/overview/application-owner-access-tokens'>dev.twitter.com</a>
Place keys in config-blank.py and rename/copy to config.py.


<h3>Run Application</h3>
```
python twitterstream.py
```
![Bash Example](https://www.dropbox.com/s/msx1au6i3i66jlj/Screenshot%202014-10-05%2021.20.40.png?dl=1 "Bash example")

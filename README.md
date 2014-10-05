TwitterStreaming
================
Python Application to use Twitter's streaming API to save tweet data to a compressed csv.gz format.

Python version 2.7

New CSV.GZ files will be added to the streamdata folder (gitignore'd by default)

<h3>Submodules</h3>
This project uses two other git repos
<ul>
<li>a href='https://github.com/ryanmcgrath/twython'>twython</a></li>
<li><a href='https://github.com/jdunck/python-unicodecsv'>Python Unicodecsv</a></li>
</ul>

These currently do not need to be installed via pip as the twitterstream.py application will import from the submodules.
Submodule requirements do need to be installed.

```
pip install requests
pip install requests_oauthlib
```

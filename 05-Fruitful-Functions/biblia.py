"""Client for Biblia API

You need an API key to use this code. 

>>> import biblia
>>> biblia.get_biblia_content('LEB', 'txt', 'Mark 4:9', 'YourKeyHere')
Content for Mark 4:9: And he said, "Whoever has ears to hear, let him hear!"
"""

# standard Python modules for working with and opening URLs
import urllib
import urllib2

# put your API key in key.py like this
# KEY = 'abcdefghi'
from key import KEY

def construct_base_url(bible, text):
    """Return the base URL for BIBLE and TEXT. 
    BIBLE is 'KJV' or 'LEB'
    TEXT is 'xml' or 'json' or 'txt'
    """
    base_url = 'http://api.biblia.com/v1/bible/content/'
    url = base_url + bible + '.' + text
    return url

def construct_url(base_url, passage, apikey=KEY):
    """Ensure URL, PASSAGE, and APIKEY are properly combined and
    encoded for opening a resource. Assumes the Bible version and
    return type are already in URL.
    """
    return base_url + '?' + urllib.urlencode({'passage': passage,
                                              'key': apikey})
    
def fetch_url(url):
    req = urllib2.urlopen(url)
    return req.read()

def print_result(passage, str):
    print('Content for', passage + ':', str)

# Now put it all together

def get_biblia_content(bible, text, passage, apikey=KEY):
    base = construct_base_url(bible, text)
    result = fetch_url(construct_url(base, passage, apikey))
    print_result(passage, result)

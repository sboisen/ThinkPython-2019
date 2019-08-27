"""Client for Biblia API

You need an API key to use this code. 

>>> import biblia
>>> biblia.get_biblia_content('LEB', 'txt', 'Mark 4:9', KEY)
Content for Mark 4:9: And he said, "Whoever has ears to hear, let him hear!"
"""

# standard Python modules for working with and opening URLs
import urllib

# put your API key in key.py like this
# KEY = 'abcdefghi'
from key import KEY

def construct_base_url(bible, format):
    """Return the base URL for BIBLE and FORMAT. 
    BIBLE is 'KJV' or 'LEB'
    FORMAT is 'xml' or 'json' or 'txt'
    """
    base_url = 'http://api.biblia.com/v1/bible/content/'
    url = base_url + bible + '.' + format
    return url

def construct_url(base_url, passage, apikey=KEY):
    """Ensure URL, PASSAGE, and APIKEY are properly combined and
    encoded for opening a resource. Assumes the Bible version and
    return type are already in URL.
    """
    return base_url + '?' + urllib.parse.urlencode({'passage': passage,
                                                    'key': apikey})
    
def fetch_url(url):
    req = urllib.request.urlopen(url)
    return req.read()

def print_result(passage, str):
    print('Content for', passage + ':', str)

# Now put it all together

def get_biblia_content(bible, format, passage, apikey=KEY):
    base = construct_base_url(bible, format)
    result = fetch_url(construct_url(base, passage, apikey))
    print_result(passage, result)

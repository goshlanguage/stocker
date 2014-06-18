#!/usr/bin/python
# From http://stackoverflow.com/questions/5081710/how-to-create-a-stock-quote-fetching-app-in-python

import urllib
import re

def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + symbol).read()
    match = re.search('id="ref_(.*?)">(.*?)<', content)
    if match:
        quote = match.group(2)
    else:
        quote = ':( Sorry, I couldn\'t find ' + symbol
    return quote

#!/usr/bin/python
# From http://stackoverflow.com/questions/5081710/how-to-create-a-stock-quote-fetching-app-in-python

from pandas_datareader import DataReader
import datetime

import urllib #3 import PoolManager
import re

def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + symbol).read()

    # Python3 compatibility (not working)
    # manager = PoolManager(num_pools=2)
    # content = manager.urlopen('GET', base_url + symbol)

    match = re.search('id="ref_(.*?)">(.*?)<', content)
    if match:
        quote = match.group(2)
    else:
        quote = ':( Sorry, I couldn\'t find ' + symbol
    return quote

def get_historic(symbol, days):
    stock = {}
    quote = DataReader(symbol, 'yahoo', datetime.datetime.today().date()-datetime.timedelta(days), datetime.datetime.today().date())
    #stock['Open'] = quote['Open']
    #stock['Close'] = quote['Close']
    #stock['High'] = quote['High']
    #stock['Low'] = quote['Low']
    #stock['Volume'] = quote['Volume']
    return quote #stock

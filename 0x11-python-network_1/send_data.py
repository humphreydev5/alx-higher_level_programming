#!/usr/bin/python3

import urllib.request
import urllib.parse

url = 'http://humphreyikhalea.tech'
values = { 'name' : 'Humphrey Ikhalea',
           'Age' : 30,
           'Lang' : 'python'
           }
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
       the_page = response.read()
       print(the_page)

#!/usr/bin/python3

import urllib.request
req = urllib.request.Request('http://www.codewithalareef.tech')
try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
        print(e.reason) 

#!/usr/bin/python3

import urllib.request
with urllib.request.urlopen("http://codewithalareef.tech") as response:
     r = response.read()
     print(r)
     print()
     for i in response.headers.items():
         print(i)
     print (response.headers["Server"])

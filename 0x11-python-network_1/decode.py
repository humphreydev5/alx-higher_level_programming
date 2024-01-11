#!/usr/bin/python3

import urllib.request
with urllib.request.urlopen("http://codewithalareef.tech") as response:
    body = response.read()
    decoded_body = body.decode("utf-8")
    print(decoded_body[5:])

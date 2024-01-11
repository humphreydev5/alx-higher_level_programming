#!/usr/bin/python3
"""
This script fetches URL
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io'
with urllib.request.urlopen(url) as r:
    content = r.read()
    print('Body response:')
    print(f'\t - type: {type(content)}')
    print(f'\t - content: {content}')
    print(f'\t - utf8 content: {content.decode("utf-8")}')

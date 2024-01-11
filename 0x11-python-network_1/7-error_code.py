#!/usr/bin/python3

"""
 Python script that takes in a URL, sends a request to the URL
 and displays the body of the response
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(f"{req.text}")

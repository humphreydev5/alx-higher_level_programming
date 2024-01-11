#!/usr/bin/python3

"""
 Python script that takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1]
    data = {"letter": q}
    req = requests.post(url, data)

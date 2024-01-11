#!/usr/bin/python3
"""
Retrieving commit message
"""

import requests
import json
import sys
user = sys.argv[1]
repo = sys.argv[2]
token = sys.argv[3]
end = f"https://api.github.com/repos/{user}/{repo}/commits"
Auth = {
        "Authorization": f"Token {token}",
        "Accept": "application/vnd.github.v3+json"
        }

res = requests.get(end, headers=Auth)
if res.status_code == 200:
    #data = json.loads(res.content)
    data = res.json()

    for commit in data:
        print(f"Commit SHA: {commit.get('sha')}")
        print(f"Message: {commit.get('commit').get('message')}")
        print(f"Auth Email: {commit.get('commit').get('author').get('email')}")
        print(f"Auth name: {commit.get('commit').get('author').get('name')}")
        print(f"commiter name: {commit.get('commit').get('committer').get('name')}")
        print(f"commit date: {commit.get('commit').get('author').get('date')}")
else:
    print("Failed to get commit history: {res.status_code}")

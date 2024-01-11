#!/usr/bin/python3

"""Write a Python script that takes 2 arguments in order to solve
this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
    res = requests.get(url)
    if res.status_code == 200:
        commits = res.json()
        for commit in commits:
            sha = commit.get('sha')
            auth = commit.get('commit').get('author').get('name')
            print(f"{res.status_code}: {sha}: {auth}")
    else:
        print(f"{res.status_code}")

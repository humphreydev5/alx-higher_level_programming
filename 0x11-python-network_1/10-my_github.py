#!/usr/bin/python3

""" a Python script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id
"""

import sys
import requests

if __name__ == "__main__":
    user_name = sys.argv[1]
    personal_token = sys.argv[2]
    Auth = {"Authorization": f"token {personal_token}"}
    url = f"https://api.github.com/users/{user_name}"
    res = requests.get(url, headers=Auth)
    if res.status_code == 200:
        user_data = res.json()
        print(f"{user_data.get('id')}")
    else:
        print('None')

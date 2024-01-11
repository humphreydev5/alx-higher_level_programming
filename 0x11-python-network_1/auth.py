#!/usr/bin/python3

import requests
import sys
personal_token = sys.argv[1]
username = sys.argv[2]
Auth = {"Authorization": f"token {personal_token}"}
url = f"https://api.github.com/users/{username}"
response = requests.get(url, headers=Auth)
if response.status_code == 200:
    user_data = response.json()
    print(f"Authenticated user_id: {user_data.get('id')}")
    print(f"email: {user_data['email']}")
    print(f"bio: {user_data['bio']}")
    print(f"public_repos: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
else:
    print("Failed to retrieve authenticated user information")

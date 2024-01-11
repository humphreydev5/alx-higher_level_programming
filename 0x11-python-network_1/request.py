#!/usr/bin/python3

import requests
#print(dir(requests.requests.__builtins__))

r = requests.get('http://codewithalareef.tech')
print(r.status_code)
print(r.text)
data = {'username': 'codewithalareef', 'email': 'john@example.com', 'password': 'password123'}
a = requests.post('https://httpbin.org/post', data)
if a.status_code == 200:
    print("User created successfully")
else:
    print(f"Error {a.status_code}")

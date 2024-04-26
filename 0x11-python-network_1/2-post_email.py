#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    body = response.read()

print("Response body (decoded in utf-8):")
print(body.decode('utf-8'))

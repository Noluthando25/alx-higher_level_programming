#!/usr/bin/python3
import requests
import sys

url = sys.argv[1]
response = requests.get(url)

if response.status_code >= 400:
    print("Error code: {}".format(response.status_code))
else:
    print("Response body:")
    print(response.text)

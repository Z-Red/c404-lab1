#!/usr/bin/python

import requests

print(requests.__version__)
print(requests.get("https://google.com").status_code)

print("\n")
print(requests.get("https://raw.githubusercontent.com/Z-Red/c404-lab1/master/main.py").text)



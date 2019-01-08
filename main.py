#!/usr/bin/python

import requests

print(requests.__version__)
print(requests.get("https://google.com").status_code)



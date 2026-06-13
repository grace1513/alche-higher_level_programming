#!/usr/bin/python3
"""Fetches the status from ALU intranet and displays the response body."""

from urllib import request

if **name** == "**main**":
with request.urlopen("https://alu-intranet.hbtn.io/status") as response:
body = response.read()
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))


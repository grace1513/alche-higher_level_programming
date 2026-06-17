#!/usr/bin/python3
"""Displays the X-Request-Id response header using requests."""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))

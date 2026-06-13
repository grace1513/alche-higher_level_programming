 request to a URL and displays the value of the X-Request-Id header."""

from urllib import request
import sys

if **name** == "**main**":
with request.urlopen(sys.argv[1]) as response:
print(response.getheader("X-Request-Id"))


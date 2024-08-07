#!/usr/bin/python3
"""
    A script that takes in a URL and
    sends a request to the URL and displays
    the value
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

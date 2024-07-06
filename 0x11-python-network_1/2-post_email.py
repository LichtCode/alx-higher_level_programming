#!/usr/bin/python3
"""A script that:
    takes in a URL sends a POST request
    to the passed URL takes email as a
    parameter and displays the body
"""
import sys
from urllib import request, parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = parse.urlencode(value).encode("ascii")

    request = request.Request(url, data)
    with request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

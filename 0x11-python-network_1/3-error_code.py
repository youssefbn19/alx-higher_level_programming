#!/usr/bin/python3
"""
    This Model contains a script that takes in a URL,
    sends a request to the URL and displays the body of the response
    (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import urllib.error
import sys
if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            data = response.read().decode("utf-8")
            print(data)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

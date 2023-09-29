#!/usr/bin/python3
"""
    This Model contains a script that takes in a URL,
    sends a request to the URL and displays the body of the response.
"""
import sys
import requests
if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")

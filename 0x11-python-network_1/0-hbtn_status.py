#!/usr/bin/python3
"""
    This Model contain script that fetch data from :
    https://alx-intranet.hbtn.io/status using urllib package
    and display some details of the body of the response
"""
import urllib.request
if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {data.decode('utf-8')}")

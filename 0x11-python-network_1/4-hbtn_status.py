#!/usr/bin/python3
"""
    This Model contains a script that fetches
    https://alx-intranet.hbtn.io/status using the package requests.
"""
import requests
if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")

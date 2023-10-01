#!/usr/bin/python3
"""
    This Model contains a script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id.
"""
import sys
import requests
if __name__ == "__main__":
    url = f"https://api.github.com/users/{sys.argv[1]}"
    header = {"Accept": "application/vnd.github+json",
              "Authorization": f"Bearer {sys.argv[2]}"}
    res = requests.get(url, headers=header)
    if res.status_code == 200:
        data = res.json()
        print(data["id"])
    else:
        print(None)

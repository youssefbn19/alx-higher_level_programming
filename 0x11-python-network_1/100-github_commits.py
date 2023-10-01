#!/usr/bin/python3
"""
    This Model contains a script that takes 2 arguments
    "repository name" and "owner name" to list latest 10 commits
    in the repository using GitHub API.
"""
import sys
import requests
if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    header = {"Accept": "application/vnd.github+json"}
    res = requests.get(url, headers=header)
    data = res.json()
    sorted_by_date = sorted(data,
                            key=lambda row: row["commit"]["author"]["date"],
                            reverse=True)
    for i in range(0, 10):
        commit = sorted_by_date[i]
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")

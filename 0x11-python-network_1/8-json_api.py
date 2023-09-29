#!/usr/bin/python3
"""
    This Model contains a script that takes  in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with the letter as a parameter.
    => The letter must be sent in the variable q
    => If no argument is given, set q=""
    => If the response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>
    Otherwise:
    => Display Not a valid JSON if the JSON is invalid
    => Display No result if the JSON is empty
"""
import sys
import requests
if __name__ == "__main__":
    try:
        data = {"q": ""}
        if len(sys.argv) > 1:
            data["q"] = sys.argv[1]
        res = requests.post("http://0.0.0.0:5000/search_user", data)
        data = res.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")

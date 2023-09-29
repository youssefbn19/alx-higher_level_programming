#!/bin/bash
# A Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sX GET -o /dev/null -w "You got me!" "0.0.0.0:5000/catch_me"

#!/bin/bash
# Sends a GET request and displays the body of a 200 response
response=$(curl -s -w "\n%{http_code}" "$1")
body=$(echo "$response" | head -n -1)
status=$(echo "$response" | tail -n 1)

if [ "$status" -eq 200 ]; then
    echo "$body"
fi

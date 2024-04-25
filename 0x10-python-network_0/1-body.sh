#!/bin/bash

# Get the URL from user input
read -p "Enter the URL: " url

# Send a GET request to the URL and display the response body for a 200 status code
response=$(curl -s -w "%{http_code}" $url)

status_code=${response: -3}

if [ $status_code -eq 200 ]; then
    content=$(curl -s $url)
    echo "Response body:"
    echo "$content"
else
    echo "Error: Received status code $status_code, unable to display response body."
fi

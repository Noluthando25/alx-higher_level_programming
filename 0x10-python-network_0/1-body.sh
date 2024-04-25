#!/bin/bash

# Get the URL from user input
read -p "Enter the URL: " url
response=$(curl -s -w "%{http_code}" $url)

status_code=${response: -3}

if [ $status_code -eq 200 ]; then
    content=$(curl -s $url)
    echo "Response body:"
    echo $content
else
    echo "Error: Unable to display response body."
fi

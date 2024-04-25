#!/bin/bash
# Get the URL from the user input
read -p "Enter the URL: " url

# Send a request to the URL and get the response body size in bytes using curl
response=$(curl -s -o /dev/null -w "%{size_download}" $url)

# Display the size of the response body in bytes
echo "Response body size: $response bytes"

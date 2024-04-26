#!/bin/bash

read -p "Enter the URL: " url
response=$(curl -s -o /dev/null -w "%{size_download}" $url)
echo "Response body size: $response bytes"

#!/bin/bash
# Get the URL from user input
read -p "Enter the URL: " url
response=$(curl -s -w "%{http_code}" $url)

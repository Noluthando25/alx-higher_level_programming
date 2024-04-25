#!/bin/bash
# Get the URL from user input
read -p "Enter the URL: " url
email="test@gmail.com"
subject="I will always be here for PLD"
response=$(curl -s -X POST -d "email=$email&subject=$subject" $url)
echo "Response body:"
echo "$response"

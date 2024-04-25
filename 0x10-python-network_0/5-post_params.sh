#!/bin/bash
# Get the URL from user input
read -p "Enter the URL: " url

# Define the data variables for the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request to the URL with the defined variables and display the response body
response=$(curl -s -X POST -d "email=$email&subject=$subject" $url)

echo "Response body:"
echo "$response"

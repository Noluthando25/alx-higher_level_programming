#!/bin/bash
read -p "Enter the URL: " url
response=$(curl -s -X POST -d "email=$email&subject=$subject" $url)


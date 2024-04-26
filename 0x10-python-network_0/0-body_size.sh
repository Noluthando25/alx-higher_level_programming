#!/bin/bash
# Get the URL from user input
response=$(curl -s -o /dev/null -w "%{size_download}" $url)


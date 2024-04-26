#!/bin/bash
# Get the URL from user input
response=$(curl -s -w "%{http_code}" $url)

#!/bin/bash
# Get url
response=$(curl -s -X POST -d "email=$email&subject=$subject" $url)


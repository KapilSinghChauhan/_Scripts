#!/bin/bash

# Check if the file is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

# Extract the unique S3 bucket names
awk -F'[/.]' '/s3.amazonaws.com/ {print $3}' "$1" | sort | uniq


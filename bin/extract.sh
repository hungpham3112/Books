#!/bin/bash

# Specify the directory path
directory="$HOME/Books"

# Enter the directory
cd "$directory" || exit

# Find ZIP files and unzip them
find . -type f -name "*.zip" | while read -r zip_file; do
  # Get the base filename without the .zip extension
  base_filename=$(basename "$zip_file" .zip)
  
  # Extract the ZIP file into the same directory
  unzip -d "$(dirname "$zip_file")" "$zip_file"
  
  # Optionally, delete the ZIP file after extraction
  # rm "$zip_file"
done

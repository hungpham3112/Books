#!/bin/bash

# Specify the directory path
directory=$(dirname "$(dirname "$0")")
# Enter the directory
cd "$directory" || exit

# Find files larger than 100MB (excluding .git directory) and compress them into ZIP archives
find . -type d -name '.git' -prune -o -type f -size +100M -print | while read -r file; do
  # Get the base filename
  base_filename=$(basename "$file")
  filename="${base_filename%.*}"
  file_directory=$(dirname "$file")
  
  # Create the ZIP archive in the same directory
  zip -j "$file_directory/$filename.zip" "$file" && rm "$file"
done

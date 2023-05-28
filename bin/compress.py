import os
import lzma
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import time

# Get the parent directory where the script is located
script_directory = Path(__file__).resolve().parent.parent

# Change to the parent directory
os.chdir(script_directory)

# Function to compress a file
def compress_file(file_path):
    if file_path.is_file() and file_path.stat().st_size > 100 * 1024 * 1024:  # 100MB in bytes
        base_filename = file_path.stem
        file_directory = file_path.parent

        # Create the compressed file with the original file extension
        compressed_file = file_directory / f"{base_filename}.xz"

        # Compress the file
        with open(file_path, "rb") as file_in, lzma.open(compressed_file, "wb", preset=9) as file_out:
            file_out.write(file_in.read())

        # Remove the original file
        file_path.unlink()

# Find files larger than 100MB (excluding .git directory) and compress them using parallel processing
with ThreadPoolExecutor() as executor:
    # Get the list of files to compress
    files_to_compress = [file_path for file_path in Path(".").rglob("*")
                         if not (file_path.is_dir() and file_path.name == ".git")]

    # Create a rolling wheel animation
    animation = "|/-\\"

    # Submit compress_file function for each file in parallel
    compress_futures = [executor.submit(compress_file, file_path) for file_path in files_to_compress]

    # Print the rolling wheel animation while compression is in progress
    while any(not future.done() for future in compress_futures):
        for char in animation:
            print(f"\rCompressing files... {char}", end="")
            time.sleep(0.1)
    
    # Print a message after compression is completed
    print("\rCompression completed.")

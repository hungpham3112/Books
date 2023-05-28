import os
import lzma
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import time

# Get the parent directory where the script is located
script_directory = Path(__file__).resolve().parent.parent

# Change to the parent directory
os.chdir(script_directory)

# Function to extract a file
def extract_file(compressed_file):
    file_directory = compressed_file.parent
    extracted_filename = compressed_file.stem

    # Remove existing extension (if any) and add .pdf extension
    extracted_filename_pdf = extracted_filename + ".pdf"

    # Create the extracted file in the same directory with the .pdf extension
    extracted_file = file_directory / extracted_filename_pdf

    # Extract the compressed file
    with lzma.open(compressed_file, "rb") as file_in, open(extracted_file, "wb") as file_out:
        file_out.write(file_in.read())

    # Remove the compressed file
    compressed_file.unlink()

# Find compressed files (with .xz extension) and extract them using parallel processing
with ThreadPoolExecutor() as executor:
    # Get the list of compressed files to extract
    compressed_files = [file_path for file_path in Path(".").rglob("*.xz")]

    # Create a rolling wheel animation
    animation = "|/-\\"

    # Submit extract_file function for each compressed file in parallel
    futures = [executor.submit(extract_file, compressed_file) for compressed_file in compressed_files]

    # Print the rolling wheel animation while extraction is in progress
    while any(not future.done() for future in futures):
        for char in animation:
            print(f"\rExtracting files... {char}", end="")
            time.sleep(0.1)
    
    # Print a message after extraction is completed
    print("\rExtraction completed.          ")

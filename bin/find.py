import os

def search_large_files(directory):
    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            dirs.remove('.git')

        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path) and os.path.getsize(file_path) > 100 * 1024 * 1024:  # 100 megabytes
                print(file_path)

# Usage example
search_large_files('.')

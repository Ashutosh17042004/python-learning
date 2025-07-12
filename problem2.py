import os

# Specify the directory path (you can change this to any path)
directory_path = '/'  # current directory

# Check if the path exists and is a directory
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    print(f"Contents of directory '{directory_path}':")
    for item in os.listdir(directory_path):
        print(item)
else:
    print(f"The path '{directory_path}' is not a valid directory.")
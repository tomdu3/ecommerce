"""Python script to remove spaces in the file names"""

import os
import sys

def rename_files(directory, recursive=False):
    """
        Rename files in a directory and its subdirectories.

        Args:
            directory (str): The directory to rename files in.
            recursive (bool): Whether to rename files in subdirectories.
    """
    for root, dirs, files in os.walk(directory):
        for filename in files:
            new_filename = filename.replace(' ', '')
            if new_filename != filename:
                old_file_path = os.path.join(root, filename)
                new_file_path = os.path.join(root, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')
        if not recursive:
            break  # Only rename files in the current directory

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-r':
            directory = os.getcwd() if len(sys.argv) == 2 else sys.argv[2]
            rename_files(directory, recursive=True)
        else:
            rename_files(sys.argv[1])
    else:
        rename_files(os.getcwd())

if __name__ == '__main__':
    main()
"""Python script to remove spaces in the file names"""

import os
import sys

def rename_files(directory, recursive=False):
    """
    Rename files in the specified directory by removing spaces from their names.

    This function traverses the given directory and renames all files by removing any spaces in their filenames.
    If the `recursive` parameter is set to True, it will also rename files in all subdirectories.

    Args:
        directory (str): The path to the directory where files will be renamed.
        recursive (bool): If True, the function will rename files in subdirectories as well. 
                            If False, only files in the specified directory will be renamed.

    Returns:
        None: This function does not return a value. It prints the old and new filenames for each renamed file.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        OSError: If an error occurs during the renaming process (e.g., permission issues).
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
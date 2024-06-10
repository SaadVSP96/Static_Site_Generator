import os
import shutil

from copystatic import copy_files_recursive


# Get the directory containing this script
script_dir = os.path.abspath(os.path.dirname(__file__))

# Define your relative paths
relative_dir_path_static = '../static'
relative_dir_path_public = '../public'

# Convert them to absolute paths
dir_path_static = os.path.join(script_dir, relative_dir_path_static)
dir_path_public = os.path.join(script_dir, relative_dir_path_public)

# Ensure the directories are normalized
dir_path_static = os.path.normpath(dir_path_static)
dir_path_public = os.path.normpath(dir_path_public)


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


main()
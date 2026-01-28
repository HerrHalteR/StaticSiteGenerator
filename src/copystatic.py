import os
import shutil

def sync_static_to_public(source, destination):
    # 1. Clean the destination first
    if os.path.exists(destination):
        print(f"Deleting {destination}...")
        shutil.rmtree(destination)
    
    print(f"Creating {destination}...")
    os.mkdir(destination)

    # 2. Start the recursive copy
    copy_recursive(source, destination)

def copy_recursive(src, dest):
    # Get everything in the current source folder
    items = os.listdir(src)

    for item in items:
        # Create full paths so Python knows exactly where to look
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        print(f"Copying: {src_path} -> {dest_path}")

        if os.path.isfile(src_path):
            # It's a file, just copy it
            shutil.copy(src_path, dest_path)
        else:
            # It's a directory, make it in the destination and dive in
            os.mkdir(dest_path)
            copy_recursive(src_path, dest_path)

# Example usage:
# sync_static_to_public("static", "public")
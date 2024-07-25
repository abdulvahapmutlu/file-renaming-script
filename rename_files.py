import os

def rename_files(directory):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        # Sort the files to maintain a consistent order
        files.sort()

        # Rename each file
        for index, file_name in enumerate(files, start=1):
            # Define the new name
            new_name = f"images_{index}{os.path.splitext(file_name)[1]}" #Change "images_" for specific name or delete for just indexing.
            
            # Get the full path for the old and new names
            old_file = os.path.join(directory, file_name)
            new_file = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} -> {new_file}')

        print("All files have been renamed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory
directory_path = "path/to/directory"

# Call the function
rename_files(directory_path)

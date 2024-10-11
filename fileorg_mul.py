import os
import shutil
import threading

# Function to move files to their respective directories based on the file extension
def move_file(file, path, extension):
    # Check if the directory for the extension exists, create if it doesn't
    if not os.path.exists(os.path.join(path, extension)):
        os.makedirs(os.path.join(path, extension))

    # Move the file to the correct directory
    shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
    print(f"Moved {file} to {extension}/")

# Main function to organize files
def organize_files(path):
    files = os.listdir(path)
    
    threads = []  # List to keep track of all threads

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]  # Remove the dot from the extension

        # Only create a thread for files (ignoring directories)
        if os.path.isfile(os.path.join(path, file)):
            # Create a new thread for each file move operation
            thread = threading.Thread(target=move_file, args=(file, path, extension))
            threads.append(thread)
            thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All files have been sorted.\n")

# Optional feature: Folder deletion based on user input
def delete_folder(path):
    ch = input("Do you want to delete a folder? Then type the extension name: ")
    folder_path = os.path.join(path, ch)
    
    # Check if the directory exists and delete it
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"The folder '{ch}' has been deleted.")
    else:
        print(f"The folder '{ch}' does not exist.")

# Get path input from the user
path = input("Enter Path: ")

# Call the organize function to start the file sorting process
organize_files(path)

# Call the delete folder function if user wants to delete any folder
delete_folder(path)

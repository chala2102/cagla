# Lab Task 3: Simple File Manager using os module
# This program shows how Python can create, rename, list, and delete files.

import os

def file_manager_demo():

    print("=== Welcome to My Mini File Manager ===\n")

    # Step 1: Show current working directory
    current_dir = os.getcwd()
    print("Right now, I am working inside this folder:")
    print(current_dir)
    print()

    # Step 2: Create a new folder
    folder_name = "lab_files"

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Nice! I created a new folder called '{folder_name}'.")
    else:
        print(f"The folder '{folder_name}' already exists, so I’ll use it.")

    print()

    # Step 3: Create three text files
    print("Now I’m creating 3 text files inside the folder...")

    file_names = ["file1.txt", "file2.txt", "file3.txt"]

    for name in file_names:
        path = os.path.join(folder_name, name)
        with open(path, "w") as file:
            file.write(f"This is {name}")
        print(f"Created -> {name}")

    print()

    # Step 4: List files
    print("Let’s see what’s inside the folder now:")

    files = os.listdir(folder_name)

    for file in files:
        print("Found:", file)

    print()

    # Step 5: Rename one file
    print("I’m going to rename file2.txt...")

    old_name = os.path.join(folder_name, "file2.txt")
    new_name = os.path.join(folder_name, "renamed_file.txt")

    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print("Done! file2.txt is now renamed to renamed_file.txt")

    print()

    # Show updated list
    print("Updated file list:")

    files = os.listdir(folder_name)

    for file in files:
        print("Now we have:", file)

    print()

    # Step 6: Cleanup
    print("Cleaning up... deleting everything I created.")

    for file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file)
        os.remove(file_path)
        print("Deleted file:", file)

    os.rmdir(folder_name)
    print("Deleted folder:", folder_name)

    print("\nAll done! My mini file manager finished its job successfully.")


# Run program
file_manager_demo()
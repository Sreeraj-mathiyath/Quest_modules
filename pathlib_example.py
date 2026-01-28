# from pathlib import Path

# p = Path("example.txt")

# print(p.exists())  # Check if the file exists
# print(p.is_file())  # Check if it's a file
# print(p.is_dir())   # Check if it's a directory
# print(p.suffix)    # Get the file extension
# print(p.stem)      # Get the file name without extension
# print(p.parent)    # Get the parent directory

# p.write_text("pathlib is awesome!")  # Write text to the file
# content = p.read_text()               # Read text from the file
# print(content)

# p.write_text(p.read_text()+"\nAdding another line using pathlib.")  # Append text
# print(p.read_text())  # Read updated contentṇ

# folder = Path(".")
# for file in folder.iterdir():
#     print(file)
# # List all files and directories in the current folder

# Path("new_folder").mkdir(exist_ok=True)  # Create a new directory existing_ok=True prevents error if it exists
# Path("new_folder/nested_folder").mkdir(parents=True, exist_ok=True)  # Create nested directories parents=True creates parent dirs if needed

# # # Rename the file  
# # p.rename("renamed_example.txt")

# # # Delete the file
# # Path("renamed_example.txt").unlink()

# # Delete the created directories
# Path("new_folder/nested_folder").rmdir()  # Remove nested folder
# Path("new_folder").rmdir()  # Remove new_folder

# with open("example.txt","w+") as f:
#     print(f.name)
#     print(f.mode)
#     print(f.closed)
    




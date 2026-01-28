# 📌 1. Checking if a File Exists
# import os

# if os.path.exists("example.txt"):
#     print("File exists")
# else:
#     print("File does not exist")

# 📌 2. Rename a File
# os.rename("oldname.txt", "newname.txt")

# 📌 3. Delete a File
# os.remove("example.txt")

# 📌 4. Create a Directory (Folder)
# os.mkdir("myfolder")

# 📌 5. Create Multiple Nested Directories
# os.makedirs("parent/child/grandchild")

# 📌 6. Remove a Directory (must be empty)
# os.rmdir("myfolder")

# 📌 7. Remove Directory with All Contents
# import shutil
# shutil.rmtree("parent")


# (Note: shutil module is used here.)

# 📌 8. List All Files and Folders
# print(os.listdir("."))


# . means current directory.

# 📌 9. Get Current Working Directory
# print(os.getcwd())

# 📌 10. Change Directory
# os.chdir("C:/Users/YourName/Desktop")

# 📌 11. Get File Size
# size = os.path.getsize("example.txt")
# print(size, "bytes")

# 📌 12. Check if Path is a File or Directory
# os.path.isfile("example.txt")   # True/False
# os.path.isdir("myfolder")       # True/False

# 📌 13. Join Paths
# full_path = os.path.join("myfolder", "subfolder", "file.txt")
# print(full_path)  # myfolder/subfolder/file.txt (or with backslashes on
# Windows)

# 📌 14. Split Path into Directory and File
# dir_name, file_name = os.path.split("myfolder/subfolder/file.txt")
# print("Directory:", dir_name)
# print("File:", file_name)

# 📌 15. Get File Extension
# name, ext = os.path.splitext("example.txt")
# print("Name:", name)
# print("Extension:", ext)
# 📌 16. Get Last Modified Time
# import time
# mod_time = os.path.getmtime("example.txt")
# print("Last Modified:", time.ctime(mod_time))

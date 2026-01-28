# # # # # f=open("filename",mode of operation)

# with open('untitled.txt','w+') as file:
#     file.write('this is a test file')
#     file.seek(0)
#     print(file.read())













# # # # f=open("one.txt")
# # # # print(f.read())
# # # # f.close()

# # # # f=open("one.txt","r")
# # # # print(f.read())
# # # # f.close()

# # # # f=open("one.txt","r")
# # # # print(f.read(3))
# # # # f.close()

# # # # f=open("one.txt","r")
# # # # print(f.read(8))
# # # # f.close()

# # # # f=open("one.txt","r")
# # # # print(f.readline())
# # # # f.close()

# # # # f=open("one.txt","r")
# # # # print(f.readlines())
# # # # f.close()

# # # # f=open("ones.txt","r")
# # # # print(f.readline())
# # # # f.close()

# # # # f=open("one.txt","w")
# # # # print(f.write("qqqqqqqqqqqqqqqqq"))
# # # # f.close()

# # # # f=open("ones.txt","w")
# # # # print(f.write("qqqqqqqqqqqqqqqqq"))
# # # # f.close()

# # # # f=open("ones.txt","r")
# # # # print(f.write("qqqqqqqqqqqqqqqqq"))
# # # # f.close()

# # # # f=open("ones.txt","w+")
# # # # f.write("rrrrrrrrrrrrrrrrr")
# # # # f.seek(0)
# # # # print(f.read())
# # # # f.close()

# # # # f=open("ones.txt","r")
# # # # f.seek(4)
# # # # print(f.tell())
# # # # print(f.read())
# # # # f.seek(8)
# # # # print(f.read())

# # # # f.close()



# # # # f=open("ones.txt","r+")
# # # # print(f.write("qqqqqqqqqqqqqqqqq"))
# # # # f.close()

# # # # f=open("ones.txt","a")
# # # # print(f.write("qqqqqqqqqqqqqqqqq"))
# # # # f.close()

# # # # f=open("two.txt","a")
# # # # print(f.write("qqqqqqqqqqqqqqqqq"))
# # # # f.close()

# # # # f=open("three.txt","x")
# # # # f.close()

# # # # f=open("three.txt","x")
# # # # f.close()

# # # import os
# # # # os.remove("three.txt")
# # # # os.removedirs("hai")
# # # # os.removedirs("hello")
# # # import shutil
# # # # shutil.rmtree("hello")
# # # shutil.rmtree("hai")


# # file = open('example.txt', 'w')
# # file.write('Hello, World!')
# # file.write('\nThis is a test file.')
# # # file.read()  # This will not work as the file is opened in write mode
# # file.close()

# # file = open('example.txt')#default is 'r' mode
# # print(file.read())#prints the content of the file
# # file.close()



# f = open('example.txt', 'r')
# print(f.tell())#prints the current position of the cursor
# f.seek(0)#moves the cursor to the beginning of the file
# print(f.read())
# f.seek(0)#moves the cursor to the beginning of the file
# print(f.read(3))#prints next 3 characters
# print(f.tell())#prints the current position of the cursor
# print(f.read(3))#prints next 3 characters
# print(f.readlines())#prints the next line
# f.close()

# # f1  = open('example.txt', 'r+')
# # print(f1.read())
# # f1.write('\n--- IGNORE ---\nThis is a test file.\n --- IGNORE ---')
# # f1.seek(0)
# # print(f1.read())
# # f1.close()

# # f2 = open('example.txt', 'w+')
# # f2.write('aaabbbcccddd\nnew line\n--- IGNORE ---\nThis is a test file2. --- IGNORE ---')
# # f2.seek(0)
# # print(f2.read())
# # f2.close()


# # f3 = open('example.txt', 'a')
# # f3.write('\nAppending a new line.')
# # f3.close()


# # f4 = open('example.txt', 'a+')
# # f4.seek(0)
# # print(f4.read())
# # f4.write('\nAdding another line at the end.')
# # f4.seek(0)
# # print(f4.read())
# # f4.close()


# # with open('example.txt', 'r') as file:
# #     content = file.read()
# #     print(content)
# # # The file is automatically closed after the with block

# # with open(r"C:\Users\HP\OneDrive\Documents\test\test.txt","r") as file:
# #     print(file.read())
# # #r - raw string


# import os
# print(dir(os))

#1. Basic File Operations

# Reading a text file
# with open('myfile.txt', 'r') as file:
#     content = file.read()
#     print(content)

# # Writing to a text file (overwrites existing content)
# with open('output.txt', 'w') as file:
#     file.write("Hello, Python!\n")
#     file.write("This is line 2")

# # Appending to a file (doesn't overwrite)
# with open('output.txt', 'a') as file:
#     file.write("\nThis line is appended")


# 2. Reading Files – Multiple Ways
# Python# Read entire file as string
# with open('data.txt', 'r') as f:
#     content = f.read()

# # Read line by line (best for large files)
# with open('data.txt', 'r') as f:
#     for line in f:
#         print(line.strip())    # strip() removes \n

# # Read all lines into a list
# with open('data.txt', 'r') as f:
#     lines = f.readlines()      # includes \n
#     lines = [line.strip() for line in f]  # cleaner

# # Read only first N lines
# with open('bigfile.txt', 'r') as f:
#     for _ in range(10):
#         print(next(f).strip())
# 3. Writing Files Safely
# Python# Write multiple lines at once
# lines = ["First line\n", "Second line\n", "Third line\n"]

# with open('shopping.txt', 'w') as f:
#     f.writelines(lines)

# # Or using print (nice because it adds \n automatically)
# with open('log.txt', 'a') as f:
#     print("Error occurred at 2025-11-19", file=f)
#     print("User tried invalid login", file=f)
# 4. Working with Different File Types
# JSON files (very common)
# Pythonimport json

# # Write JSON
# data = {"name": "Alice", "age": 30, "cities": ["Paris", "Tokyo"]}
# with open('person.json', 'w') as f:
#     json.dump(data, f, indent=4)    # indent for pretty printing

# # Read JSON
# with open('person.json', 'r') as f:
#     data = json.load(f)
#     print(data["name"])
# CSV files
# Pythonimport csv

# # Writing CSV
# with open('people.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Name', 'Age', 'City'])
#     writer.writerows([
#         ['Bob', 25, 'Berlin'],
#         ['Carol', 30, 'London']
#     ])

# # Reading CSV
# with open('people.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# Binary files (images, PDFs, etc.)
# Python# Copy an image
# with open('photo.jpg', 'rb') as src:
#     with open('copy.jpg', 'wb') as dst:
#         dst.write(src.read())

# # Or copy in chunks (better for huge files)
# with open('bigvideo.mp4', 'rb') as src:
#     with open('copy.mp4', 'wb') as dst:
#         while chunk := src.read(1024*1024):  # 1 MB chunks
#             dst.write(chunk)
# 5. Using pathlib (Modern Python ≥3.4 – RECOMMENDED)
# Pythonfrom pathlib import Path

# file = Path('myfolder/data.txt')

# # Create directories if needed
# file.parent.mkdir(parents=True, exist_ok=True)

# # Write
# file.write_text("Hello pathlib!", encoding='utf-8')

# # Read
# content = file.read_text(encoding='utf-8')

# # Check if exists, get size, etc.
# print(file.exists())
# print(file.stat().st_size)   # size in bytes
# 6. Real-World Example: Safe File Processing
# Pythonfrom pathlib import Path
# import json

# def save_user_data(username: str, score: int):
#     file = Path('scores') / f"{username}.json"
#     file.parent.mkdir(exist_ok=True)
    
#     data = {"username": username, "high_score": score, "last_played": "2025-11-19"}
    
#     try:
#         file.write_text(json.dumps(data, indent=2))
#         print("Score saved!")
#     except Exception as e:
#         print(f"Failed to save: {e}")

# # Usage
# save_user_data("player123", 99999)


# search_word='python'
# with open("example.txt",'r') as f:
#     for line in f:
#         if search_word.lower() in line.lower():
#             print(line.strip())

# with open("example.txt",'r') as f:
#     for line in f:
#         word_list = line.strip().split()
#         print(f"number of words in {line} is {len(word_list)}")
        

# list1=["Hello world", "Python is fun", "File handling example"]
# with open("sample.txt",'w+') as file:
#     for line in list1:
#         file.write(line+"\n")
#     file.seek(0)
#     print(file.read())

# with open("sample.txt",'r') as f:
#     count=1
#     for line in f:
#         print(line if count%2!=0 else "")
#         count+=1

# with open("sample.txt",'r') as f:
#     lines= f.readlines()

# for line in lines[::2]:
#     print(line.strip())

# with open("sample.txt","w+") as file:
#     for i in range(0,101):
#         file.write(str(i)+'\n')
#     file.seek(0)
#     print(file.read())

# count=0
# with open("example.txt",'r') as file:
#     for lines in file:
#         for line in lines:
#             count+=1
# print(count)
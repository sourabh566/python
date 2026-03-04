import os

# specify the directory path
path = "/resume"

# get list of files and directories
files = os.listdir(path)

# print the contents
print("Contents of directory:")
for file in files:
    print(file)
# hum chatgpt ka use krenge and isse 4th question ko copy krenge chatgpt mai vo hmme dega usse hum vs code mai copy krenge
# or hum directory ke path mai slash denge only
#  or fr run





import os

#  Specify the dictionary you want to list
directory_path = '/'

# list all files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)
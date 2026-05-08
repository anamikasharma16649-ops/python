
import os

#  Select the directory whose content you want to list
directory_path = '/'

#  use os module to list the directory content
contents = os.listdir(directory_path)

#  print the contents of the directory
print(contents)
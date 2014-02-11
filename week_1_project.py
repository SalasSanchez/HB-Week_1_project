import shutil
import os



#1. Create 26 directories in the current directory, one for each letter of the alphabet:
# range for ascii lowercase letters is 97 through 122

for i in range(97, 123):
    os.mkdir("files_" + chr(i))

# 2. Loop through all the files in the original_files directory, and organize each of those files
 # into the directory that their name starts with.

"""
loop where x is the filename, i is the first letter of the filename
shutil.move("original_files/" + x, "files_" + x[0])
"""   

file_path = "original_files/"

for x in os.listdir(file_path):
    shutil.move(file_path + x, "files_" + x[0])


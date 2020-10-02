# Driver Program

import os
import shutil

file = 'C:\\Personal\\Work\\Directory Organiser\\temp.txt'
destination = 'C:\\Personal\\Work\\Directory Organiser\\Destination\\'

if not os.path.isdir(destination):
    os.makedirs(destination)
    print(f"New Folder Created in :{destination}")

shutil.move(file, destination)


# Driver Program

import os
import shutil

file = 'C:\\Personal\\Work\\Directory Organizer\\temp.txt'
destination = 'C:\\Personal\\Work\\Directory Organizer\\Destination\\'

if not os.path.isdir(destination):
    os.makedirs(destination)
    print(f"New Folder Created in :{destination}")

shutil.move(file, destination)


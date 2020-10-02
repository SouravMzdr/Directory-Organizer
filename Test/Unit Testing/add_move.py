# Driver Program

import os
import shutil

file = 'C:\\Personal\\Work\\Move Files\\temp.txt'
destination = 'C:\\Personal\\Work\\Move Files\\Destination\\'

if not os.path.isdir(destination):
    os.makedirs(destination)
    print(f"New Folder Created in :{destination}")

shutil.move(file, destination)


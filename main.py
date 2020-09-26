# Importing Libraries

import shutil
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join

# Setting Home Directory Path

## homedir = os.environ['HOME']
## print (homedir)
homedir = str(Path.home())

# Set the Source Direcory Path [i.e the Downloads Path]

## Change the "/Downloads" path to any other appropriate path if this script is required to run in that Directory
source = os.path.join(homedir, 'Downloads')
all_files = [f for f in listdir(source) if isfile(join(source, f))]

# List Containing the files to be Moved

documents = []
pictures = []
media = []

# Including All Types of File Extensions Possible

## Adding file extension in required places to include that files in that directory
picture_ext = ['.jpeg', '.jpg', '.png', '.bnp', '.tiff']
document_ext = ['.txt', '.md', '.pdf', '.doc', '.odt', '.docx', '.xls', '.xlsx', '.csv', '.tex', '.ppt', '.pptx', '.rtf', '.wpd']
media_ext = ['.mp3', '.mp4', '.mpeg', '.wav', '.wma', '.3gp', '.avi', '.mkv', '.mov']

## Adding CAPS Extensions too
picture_ext += [i.upper() for i in picture_ext]
document_ext += [i.upper() for i in picture_ext]
media_ext += document_ext

# Searching for Files and Categorising

for files in all_files:
    if files.endswith(picture_ext):
        pictures.append(files)
    elif files.endswith(document_ext):
        documents.append(files)
    elif files.endswith(media_ext):
        media.append(files)

# Display Functions to Print Operation [Show Moved Files]

def show_moved_documents():
    print(f"{len(documents)} Files moved to Documents!")
    for document in documents:
        print (document)

def show_moved_pictures():
    print(f"{len(pictures)} Files moved to Pictures!")
    for picture in pictures:
        print (picture)

def show_moved_media():
    print(f"{len(media)} Files moved to Media!")
    for music in media:
        print (music)

# Functions Handling the Moving Mechanism

def move_to_document():
    destination = os.path.join(homedir, 'Documents')
    print("Moving Documents ...")
    for document in documents:
        shutil.move(os.path.join(source, document), destination)
    show_moved_documents()

def move_to_pictures():
    destination = os.path.join(homedir, 'Pictures')
    print("Moving Pictures ...")
    for picture in pictures:
        shutil.move(os.path.join(source, picture), destination)
    show_moved_pictures()

def move_to_media():
    destination = os.path.join(homedir, 'Media')
    print("Moving Media Files ...")
    for music in media:
        shutil.move(os.path.join(source, music), destination)
    show_moved_media()

# Condition to Check if Required Files are Present [for Moving] and are Calling Appropriate Functions

if len(documents) != 0:
    move_to_document()
else:
    print("No Documents to Move!")

if len(pictures) !=0:
    move_to_pictures()
else:
    print("No Pictures to Move!")

if len(media) != 0:
    move_to_media()
else:
    print("No Media Files to Move!")

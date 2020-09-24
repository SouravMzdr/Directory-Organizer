import shutil
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join

#Set home directory path
#homedir = os.environ['HOME']
#print (homedir)
homedir = str(Path.home())

#Set the soource direcory path i.e the Downloads path
#Change the "/Downloads" path to any other appropriate path if this script is required to run in that directory
source = os.path.join(homedir,'Downloads')
all_files= [f for f in listdir(source) if isfile(join(source, f))]

#List containing the files to be moved
documents=[]
pictures=[]
musics=[]

#ALl file extensions
#Add file extension in required places to include that files in that directory
picture_ext=('.jpeg','.jpg','.png','.bnp','.tiff')
document_ext=('.txt','.pdf','.doc','.odt','.docx','.xls','.xlsx','.tex','.ppt','.rtf','.wpd')
music_ext=('.mp3','.mp4','.mpeg','.wav','.wma','.3gp','.avi','.mkv','.mov')

#Searching and categorising
for files in all_files:
    if files.endswith(picture_ext):
        pictures.append(files)
    elif files.endswith(document_ext):
        documents.append(files)
    elif files.endswith(music_ext):
        musics.append(files)

#Functions to show moved files
def show_moved_documents():
    print("Files moved to Documents:")
    for document in documents:
        print (document)

def show_moved_pictures():
    print("Files moved to Pictures:")
    for picture in pictures:
        print (picture)

def show_moved_musics():
    print("Files moved to Musics:")
    for music in musics:
        print (music)

#functions handling the moving mechanism
def move_to_document():
    destination = os.path.join(homedir,'Documents')
    for document in documents:
        shutil.move(os.path.join(source,document),destination)
    show_moved_documents()

def move_to_pictures():
    destination = os.path.join(homedir,'Pictures')
    for picture in pictures:
        shutil.move(os.path.join(source,picture),destination)
    show_moved_pictures()

def move_to_musics():
    destination = os.path.join(homedir,'Music')
    for music in musics:
        shutil.move(os.path.join(source,music),destination)
    show_moved_musics()


#Condition to check if required files are present and call appropriate functions
if len(documents)!=0:
    move_to_document()
else:
    print("No Documents to move")

if len(pictures)!=0:
    move_to_pictures()
else:
    print("No Pictures to move")

if len(musics)!=0:
    move_to_musics()
else:
    print("No Music to move")

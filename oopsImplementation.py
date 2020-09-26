# Importing Libraries

import shutil
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join

# Class 'Move Files'
class move_files:

    # Constructor
    def __init__(self, path = 'Downloads'):

        # Setting Home Directory Path
        self.homedir = str(Path.home())

        # Set the Source Direcory Path [i.e the Downloads Path by DEFAULT]
        self.source = os.path.join(self.homedir, path)
        self.all_files = [f for f in listdir(self.source) if isfile(join(self.source, f))]
        ## NOTE - We can Change the "/Downloads" path to any other appropriate path if this script is required to run in that Directory

        # List Containing the files to be Moved
        self.documents = []
        self.pictures = []
        self.musics = []
        self.videos = []

        # Including All Types of File Extensions Possible

        ## Adding file extension in required places to include that files in that directory
        self.picture_ext = ['.jpeg', '.jpg', '.png', '.bnp', '.tiff', '.gif']
        self.document_ext = ['.txt', '.md', '.pdf', '.doc', '.odt', '.docx', '.xls', '.xlsx', '.csv', '.tex', '.ppt', '.pptx', '.rtf', '.wpd']
        self.music_ext = ['.mp3', '.mpeg', '.wav', '.wma', '.3gp', '.aac', '.wma']
        self.video_ext = ['.mp4', '.avi', '.mkv', '.mov', '.flv']

        ## Adding CAPS Extensions too
        self.picture_ext += [i.upper() for i in self.picture_ext]
        self.document_ext += [i.upper() for i in self.picture_ext]
        self.music_ext += [i.upper() for i in self.music_ext]
        self.video_ext += [i.upper() for i in self.video_ext]

        # Extracting Information about the Files Present
        self.extractingFiles()


    # Function which extracts Information about the Files Present

    def extractingFiles(self):

        # Searching for Files and Categorising
        for files in self.all_files:

            if files.endswith(tuple(self.picture_ext)):
                self.pictures.append(files)
            elif files.endswith(tuple(self.document_ext)):
                self.documents.append(files)
            elif files.endswith(tuple(self.music_ext)):
                self.musics.append(files)
            elif files.endswith(tuple(self.video_ext)):
                self.videos.append(files)


    # Display Functions to Print Operation [Show Moved Files]
        
    def show_Moved_Documents(self):

        print(f"{len(self.documents)} Files moved to Documents!")
        for document in self.documents:
            print(document)

    def show_Moved_Pictures(self):

        print(f"{len(self.pictures)} Files moved to Pictures!")
        for picture in self.pictures:
            print(picture)

    def show_Moved_Music(self):

        print(f"{len(self.musics)} Files moved to Music!")
        for music in self.musics:
            print(music)
        
    def show_Moved_Videos(self):

        print(f"{len(self.videos)} Files moved to Videos!")
        for video in self.videos:
            print(video)


    # Functions Handling the Moving Mechanism

    def move_To_Document(self):

        destination = os.path.join(self.homedir, 'Documents')
        self.checkDirExists(destination)
        print("Moving Documents ...")
        for document in self.documents:
            shutil.move(os.path.join(self.source, document), destination)
        self.show_Moved_Documents()

    def move_To_Pictures(self):

        destination = os.path.join(self.homedir, 'Pictures')
        self.checkDirExists(destination)
        print("Moving Pictures ...")
        for picture in self.pictures:
            shutil.move(os.path.join(self.source, picture), destination)
        self.show_Moved_Pictures()

    def move_To_Music(self):

        destination = os.path.join(self.homedir, 'Music')
        self.checkDirExists(destination)
        print("Moving Music Files ...")
        for music in self.music:
            shutil.move(os.path.join(self.source, music), destination)
        self.show_Moved_Music()

    def move_To_Video(self):

        destination = os.path.join(self.homedir, 'Videos')
        print("Moving Video Files ...")
        for video in self.videos:
            shutil.move(os.path.join(self.source, video), destination)
        self.show_Moved_Videos()


    # Condition to Check if Required Files are Present [for Moving] and are Calling Appropriate Functions

    def checkCondition(self):

        if len(self.documents) != 0:
            self.move_To_Document()
        else:
            print("No Documents to Move!")

        if len(self.pictures) !=0:
            self.move_To_Pictures()
        else:
            print("No Pictures to Move!")

        if len(self.music) != 0:
            self.move_To_Music()
        else:
            print("No Music Files to Move!")

        if len(self.videos) != 0:
            self.move_To_Video()
        else:
            print("No Videos to Move!")

    
    # Check for Existence of a Directory
    
    def checkDirExists(self, path):

        if not path:
            os.makedirs(path)

    
# Main Function
def main():
    
    print("Enter the Full Path to your Directory [Ignore if 'Downloads']")
    path = input()
    if path == None:
        moveFilesObject = move_files()
    else:
        moveFilesObject = move_files(path)
    moveFilesObject.checkCondition()


# Main Method
if __name__ == '__main__':
    main()
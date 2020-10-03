# Importing Libraries

import shutil
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join
import time


# Class 'Move Files'
class directoryOrganizer:

    # Constructor
    def __init__(self, path = None, verbose = False):

        # Checking Condition for Default Argument
        if not path:

            path = "Downloads"

            # Setting Home Directory Path
            self.homedir = str(Path.home())

            # Set the Source Directory Path [i.e the Downloads Path by DEFAULT]
            self.source = os.path.join(self.homedir, path)

        else:

            # Set the Source Directory Path [when Path isn't Downloads]
            self.source = os.path.join(path)

        # Copying All Files Names Present in the Source Directory
        self.all_files = [f for f in listdir(self.source) if isfile(join(self.source, f))]

        ## NOTE - We can Change the "/Downloads" path to any other appropriate path if this script is required to run in that Directory

        # List Containing the files to be Moved
        self.documents = []
        self.pictures = []
        self.musics = []
        self.videos = []
        self.others = []

        # Including All Types of File Extensions Possible

        ## Adding file extension in required places to include that files in that directory
        self.picture_ext = ['.jpeg', '.jpg', '.png', '.bnp', '.tiff', '.gif']
        self.document_ext = ['.txt', '.md', '.pdf', '.doc', '.odt', '.docx', '.xls', '.xlsx', '.csv', '.tex', '.ppt',
                             '.pptx', '.rtf', '.wpd']
        self.music_ext = ['.mp3', '.mpeg', '.wav', '.wma', '.3gp', '.aac', '.wma']
        self.video_ext = ['.mp4', '.avi', '.mkv', '.mov', '.flv']

        ## Adding CAPS Extensions too
        self.picture_ext += [i.upper() for i in self.picture_ext]
        self.document_ext += [i.upper() for i in self.picture_ext]
        self.music_ext += [i.upper() for i in self.music_ext]
        self.video_ext += [i.upper() for i in self.video_ext]

        # Flag if the User wants to Print the Files that are been moved
        self.flag = verbose

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
            else:
                self.others.append(files)
        
        #### For Testing Purpose Only
        print(f"For Pictures : {len(self.pictures)}")
        print(f"For Documents : {len(self.documents)}")
        print(f"For Musics : {len(self.musics)}")
        print(f"For Videos : {len(self.videos)}")
        print(f"For Others : {len(self.others)}")


# Package Class
class organizer:

    # Constructor
    def __init__(self, path = None, verbose = False):

        # Intitialising Class Variables

        self.path = path
        self.verbose = verbose
        self.moveFilesObject = None                                      # Class Object

        # Using Error Handling Techniques to Handle Error(s)

        try:
            start = time.time()
            self.moveFilesObject = directoryOrganizer(self.path, self.verbose)
            # self.moveFilesObject.checkCondition()
            end = time.time()
            print('Time Elapsed : ', round(end - start, 2), 'seconds')

        except Exception as exception:

            print("Please Try Again! An Unexpected Error has Occurred!")
            print(f"Type : {type(exception)}")
            print(f"Error : {exception}")


# Main Method
if __name__ == '__main__':
    classObject = organizer('C:\Personal\Work\Directory Organiser\Test\Random', True)

## Conlusion => Unit Testing Successful for constructorCheck.
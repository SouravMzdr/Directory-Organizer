# Importing Libraries

import shutil
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join

# Class 'Move Files'
class directoryOrganiser:

    # Constructor
    def __init__(self, path = None):

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
        self.document_ext = ['.txt', '.md', '.pdf', '.doc', '.odt', '.docx', '.xls', '.xlsx', '.csv', '.tex', '.ppt', '.pptx', '.rtf', '.wpd']
        self.music_ext = ['.mp3', '.mpeg', '.wav', '.wma', '.3gp', '.aac', '.wma']
        self.video_ext = ['.mp4', '.avi', '.mkv', '.mov', '.flv']

        ## Adding CAPS Extensions too
        self.picture_ext += [i.upper() for i in self.picture_ext]
        self.document_ext += [i.upper() for i in self.picture_ext]
        self.music_ext += [i.upper() for i in self.music_ext]
        self.video_ext += [i.upper() for i in self.video_ext]

        # Flag if the User wants to Print the Files that are been moved
        self.flag = None

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


    # Display Functions to Print Operation(s) [Show Moved Files] [Flag]
        
    def show_Moved_Documents(self):

        print(f"{len(self.documents)} Files moved to Documents!")
        if self.flag.lower() == 'yes':
            for document in self.documents:
                print(document)

    def show_Moved_Pictures(self):

        print(f"{len(self.pictures)} Files moved to Pictures!")
        if self.flag.lower() == 'yes':
            for picture in self.pictures:
                print(picture)

    def show_Moved_Music(self):

        print(f"{len(self.musics)} Files moved to Music!")
        if self.flag.lower() == 'yes':
            for music in self.musics:
                print(music)
        
    def show_Moved_Videos(self):

        print(f"{len(self.videos)} Files moved to Videos!")
        if self.flag.lower() == 'yes':
            for video in self.videos:
                print(video)

    def show_Moved_Others(self):
    
        print(f"{len(self.others)} Files moved to Others!")
        if self.flag.lower() == 'yes':
            for other in self.others:
                print(other)


    # Functions Handling the Moving Mechanism

    def move_To_Document(self):

        destination = os.path.join(self.source, 'Documents')
        self.checkDirExists(destination)
        print("Moving Documents ...")
        for document in self.documents:
            shutil.move(os.path.join(self.source, document), destination)
        self.show_Moved_Documents()

    def move_To_Pictures(self):

        destination = os.path.join(self.source, 'Pictures')
        self.checkDirExists(destination)
        print("Moving Pictures ...")
        for picture in self.pictures:
            shutil.move(os.path.join(self.source, picture), destination)
        self.show_Moved_Pictures()

    def move_To_Music(self):

        destination = os.path.join(self.source, 'Music')
        self.checkDirExists(destination)
        print("Moving Music Files ...")
        for music in self.musics:
            shutil.move(os.path.join(self.source, music), destination)
        self.show_Moved_Music()

    def move_To_Videos(self):

        destination = os.path.join(self.source, 'Videos')
        self.checkDirExists(destination)
        print("Moving Video Files ...")
        for video in self.videos:
            shutil.move(os.path.join(self.source, video), destination)
        self.show_Moved_Videos()

    def move_To_Others(self):

        destination = os.path.join(self.source, 'Others')
        self.checkDirExists(destination)
        print("Moving Other File Extensions ...")
        for other in self.others:
            shutil.move(os.path.join(self.source, other), destination)
        self.show_Moved_Others()


    # Condition to Check if Required Files are Present [for Moving] and are Calling Appropriate Functions

    def checkCondition(self):

        ## Sets the Flag whether to Print the Files Names of the Moved Files
        self.flag = input("Do you want to Display the File Names? (YES/NO) : ")

        ## Check for whether the files exists for a Particular Category or Not

        if len(self.documents) != 0:
            self.move_To_Document()
        else:
            print("No Documents to Move!")

        if len(self.pictures) != 0:
            self.move_To_Pictures()
        else:
            print("No Pictures to Move!")

        if len(self.musics) != 0:
            self.move_To_Music()
        else:
            print("No Music Files to Move!")

        if len(self.videos) != 0:
            self.move_To_Videos()
        else:
            print("No Videos to Move!")

        if len(self.others) != 0:
            self.move_To_Others()
        else:
            print("No Miscellaneous Files to Move!")

    
    # Check for Existence of a Directory [if it DNE, creates a New One]
    
    def checkDirExists(self, path):

        if not os.path.isdir(path):
            os.makedirs(path)


# Main Function
def main():

    # Using Error Handling Techniques to Handle Error(s)
    
    try:

        print('''
Where do you want to Organise your Files?
1. Downloads
2. Any Other Location
Enter the Full Path to your Directory [Just Type 'Downloads' for Case 2] ->
        ''')
        path = input()
        moveFilesObject = directoryOrganiser(path)
        moveFilesObject.checkCondition()

    except:

        print("Please Try Again! An Unexpected Error has Occurred!")


# Main Method
if __name__ == '__main__':
    main()
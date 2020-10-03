# Importing Class
from oopsImplementation import directoryOrganizer

# Importing Libraries
import time


# Package Class
class organizer:

    # Constructor
    def __init__(self, path = None, verbose = False):

        # Initialising Class Variables

        self.path = path
        self.verbose = verbose
        self.moveFilesObject = None  # Class Object

        # Using Error Handling Techniques to Handle Error(s)

        try:
            start = time.time()
            self.moveFilesObject = directoryOrganizer(self.path, self.verbose)
            self.moveFilesObject.checkCondition()
            end = time.time()
            print('Time Elapsed : ', round(end - start, 2), 'seconds')

        except Exception as exception:

            print("Please Try Again! An Unexpected Error has Occurred!")
            print(f"Type : {type(exception)}")
            print(f"Error : {exception}")

    # Method to Get Moved Files History
    def showHistory(self, extension_type = None):

        return self.moveFilesObject.showHistory(extension_type)


# Commenting out for Packaging.


# Main Method
if __name__ == '__main__':
    #path = 'C:\Personal\Work\Directory Organizer\Test\Random'
    #classObject = organizer(path, True)
    organizer('C:\\Users\\rahul.bordoloi\\Desktop\\123')
    #print(classObject.showHistory('Others'))




# Importing Class
from oopsImplementation import directoryOrganiser

# Importing Libraries
import time


# Main Function
def main():

    # Using Error Handling Techniques to Handle Error(s)
    try:

        start = time.time()
        print('''
Where do you want to Organise your Files?
1. Downloads
2. Any Other Location
Enter the Full Path to your Directory [Just Type 'Downloads' for Case 2] ->''')
        path = input()
        moveFilesObject = directoryOrganiser(path)
        moveFilesObject.checkCondition()
        end = time.time()
        print('Time Elapsed : ', round(end - start, 2), 'seconds')

    except:

        print("Please Try Again! An Unexpected Error has Occurred!")


# Main Method
if __name__ == '__main__':
    main()
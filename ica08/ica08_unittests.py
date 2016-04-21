import unittest                                                          # Imports the test library 
import time                                                              # Imports the time module
import os                                                                # Imports the module that helps us close a picture (taskkill)
from PIL import Image                                                    # Library to help us opening the pictures


# Testing the time module. Aim is to loop a print message 4
# times with 2 seconds delay. Therfor we give it the value of 4
waitTwoSeconds = 4       


class TimeTest(unittest.TestCase):                                       # Creates the test class to test our various functions
    def testTime(self):
        print "I will print out new messages every two seconds, and no more than 4"
        for i in range(waitTwoSeconds):                                  # Prints out equally amount of messages of what chosen in waitTwoSeconds def
            time.sleep(2)                                                # Waits two seconds before printing and counting
            print "Two seconds have passed"

    
    def testPictureLoader(self):
        print "I will show two different pictures for two seconds. Only one picture should be vissible at same time"
        img = Image.open("unittest_1.jpg")                               # Loads the image into memory
        img.show()                                                       # Open the image currently stored in memory
        time.sleep(2)
        # The following sollution is really, really bad. The issue we encountered was that 
        # the function img.close() or Image.close() did not work. Therfor the sollution 
        # was to find the picture display in task manager and kill it with help of python. 
        # I anticipate that this will not work on other systems than Windows 10, since
        # the process likely goes under other names on other OS, and depends on what
        # program you use to open images of .jpg type
        os.system("taskkill /im dllhost.exe")   
        
        img = Image.open("unittest_2.jpg")
        img.show()
        time.sleep(2)
        os.system("taskkill /im dllhost.exe")
        print "If the function works as planned, no pictures should be shown on the screen at the time of this message"
        print ""                                                         # Gives us an extra line between this test case and the other
        

        
def main():
    unittest.main()
    
    
if __name__ == "__main__":
    main()
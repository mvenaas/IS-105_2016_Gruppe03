"""This project contains the code that simulates a virtual file system. The system will take user inputs to simulate a simple file system"""
import sys                                                      # Imports function from the "SYS" module which we will use later in the code

virtualMemory = []                                              # Creates the virtual system's memory, RAM
virtualDisk = [1, 2, 3, 4, 5, 6, 7, 8]                          # Serves as the virtual harddrive
FAT = []

for i in (virtualDisk):                                         # Not done with this yet. The idea is to assign the files on the hard drive to an ID or
        FAT.append(i)                                           # number / index on the FAT. This way the FAT will be linked togheter with the files stored
print FAT                                                       # and work togheter with the virtualDiskLimit

virtualDiskLimit = 8                                            # The virtual disk can contain no more than 8 items
virtualDiskCommands = ["DELETE", "SAVE"]


print "Welcome to this virtual filesystem."                     # Prints the welcome message to the user, letting him / her know the system is operational 
print "The system is currently idle and awaiting commands"


def openingCondition():                                         # Creates the opening condition, takes the user input into an conditional
        print "Ready to start? Yes / no"
        userInput = raw_input()                                 # The input, or commmand word if you like, from the user. Works as command words
        userInput = userInput.upper()                           # Changes the input to upper case letters to eliminate mismatch / errors on input
        print ""                                                # Prints an extra line to prevent cluster of information  
        if userInput == "NO":
                print "closing..."
                sys.exit()                                      # Closes the program
        else:
                print "Great! Moving on..."
                print ""                                        # Prints an extra line to prevent cluster of information
openingCondition()                                              # Performs the function call to ensure the program runs it. 


def saveOrDelete():
        print "Want to save or delete elements to the disk? Save and delete are the keywords"
        saveOrDeleteQuestion = raw_input()
        saveOrDeleteQuestion = saveOrDeleteQuestion.upper()
        if saveOrDeleteQuestion == "SAVE":
                print "Moving on to the save function"
                print ""                                        # The program will now move to saveToVirtualDisk function
        elif saveOrDeleteQuestion == "DELETE":
                print "Removed last item added to the disk"
                print ""
                virtualDisk.pop()                              # Removing the item currently stored on index 7 in virtualDisk list (list is from 0 - 7)
        else:
                print ""
                print "Use save or delete keywords only. Try again"
                print ""
                saveOrDelete()
saveOrDelete()                                                  # Starting the saveOrDelete function
                                             
    
def saveToVirtualDisk():                                        # Function to add elements to our virtual harddrive. Same as before, using the users input
        print "Save an file to the disk? Yes / No"
        saveToDisk = raw_input()
        saveToDisk = saveToDisk.upper()
        print ""                                                # Again, extra line for better visual look
        if saveToDisk == "NO":                                  # Here we ask a new question, giving the user more options rather than just stopping the program
                print "That's allright, want to continue (yes) or quit program (no)?"
                questionTwo = raw_input()                       # New variable name, to ensure we get only one input to check on
                questionTwo = questionTwo.upper()
                print ""
                if questionTwo == "NO":
                        print "closing..."
                        print ""
                        sys.exit()                              # Closes the program
                else: 
                        print "Continue on!"
                        print ""
                        saveToVirtualDisk()                     # Starts the function again. Ideally this should do something else. Will come back to this later
        else:    
                if len(virtualDisk) >= virtualDiskLimit:        # Check if the hard drive is full (capasity is up to 8 integers). If so, exiting the program
                        print "The hard drive is full. Want to delete a file or quit program?"
                        print ""
                        questionThree = raw_input()
                        questionThree = questionThree.upper()
                        if questionThree == "DELETE":
                                print "Last file added to the drive is now deleted, current files stored on disk: "
                                virtualDisk.pop()               # removes int stored on last index of the list
                                print virtualDisk
                                print ""
                                print "Continue, or close program? Yes / no"
                                questionFour = raw_input()
                                if questionFour == "yes":
                                        print "Starting over..."
                                        print ""
                                        saveToVirtualDisk()
                                else: 
                                        print "Exiting..."
                                        print ""
                                        sys.exit(0)
                        else:
                                print "Exiting program"
                                sys.exit(0)                     # Exits the program
                else:
                        addNumber = input("what file will we store to the disk?")
                        virtualDisk.append(addNumber)
                        print "Currently we have following files on the disk:"
                        print virtualDisk    
                        print ""       
                        saveToVirtualDisk()                     # Making the program loop. To be improved
saveToVirtualDisk()                                             # Calling the function








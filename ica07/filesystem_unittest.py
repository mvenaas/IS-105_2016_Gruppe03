import unittest                                                                 # Imports the test library 


virtualDisk = [1, 2, 3, 4, 5, 6, 7, 8]                                          # This is the list we're testing, and we fill it up with the numbers 1 - 8


class FilesystemTests(unittest.TestCase):                                       # Creates the test class to test our various functions
    def fillVirtualDisk(self):
        self.assertEquals(virtualDisk, [1, 2, 3, 4, 5, 6, 7, 8])                # First it checks the virtualDisk, then compare it with these numbers to see if they match
                                                                                # If they match it means the function is working as it should and assigns the right numbers
                                                                                # to the virtualDisk variable
    print "The test checks if virtualDisk is: [1, 2, 3, 4, 5, 6, 7, 8]"         # Simple printline, to tell us what is going on
    
        
def main():
    unittest.main()
    
    
if __name__ == "__main__":
    main()
    
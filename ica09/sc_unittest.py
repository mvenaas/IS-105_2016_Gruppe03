import unittest                                                         # Imports the test library 
from socket import *                                                    # Imports the needed modules for client / server testing
import sys
import select
import os
import subprocess

address = ('localhost', 6005)                                           # The adress and port used for the testing
server_socket = socket(AF_INET, SOCK_DGRAM)                             # Establish the socket
server_socket.bind(address)                                             # Binds the socket and adress, which keeps an connection open to the user client
connected = False                                                       # An boolean check. False by default, but changes to True when there is an connection

class connectionTest(unittest.TestCase):                                # Creates the test class to test our various functions
    
    while(connected == False):                                          # As long as the server has not recieved the ready signal from the client, continue listening
        print "Please start the client.py file to complete the test"
        recv_data, addr = server_socket.recvfrom(2048)
        
        # Below are the settings for the server, and depending on the information recieved 
        # two possible outcomes may occure. Test should ideally beeing passed on first condition
        if recv_data == "Connected" :
            connected = True                                            # If an connection is made, change this boolean to True which affects the main RiverCrossing program
            print "The test passed"
            data = "testPassed"
            server_socket.sendto("Connected", addr)
            
        elif recv_data == "" :                                          # Again, this should under normal circumstances not happen
            connected = False
            print "Failed to connect"
            data = "testFailed"
            server_socket.sendto(data, addr)        
        
        
def main():
    unittest.main()
    
    
if __name__ == "__main__":
    main()
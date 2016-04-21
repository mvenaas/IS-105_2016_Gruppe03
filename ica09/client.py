from socket import *                                        # Impots the needed modules for the client / server module to work correctly
import sys
import select

print "Welcome to the client. Write start to connect to the server"
print "or write close to stop the program"
startClient = raw_input()
startClient = startClient.lower()
print "Recieved: ", startClient

address = ('localhost', 6005)                                   # Connects the client with the server
client_socket = socket(AF_INET, SOCK_DGRAM)

if startClient == "start": 
    num_retransmits = 0                                         # Helps iterate, ideally only tries one time
    while(num_retransmits < 1):
        num_retransmits = num_retransmits + 1                   # Increase variable with one to complete the cycle


        data = "Connected"                                      # Sends information to the server, which use it as a condition
        client_socket.sendto(data, address)

        recv_data, addr = client_socket.recvfrom(2048)

        #print recv_data, "!!"                                  # Not using this at current time beeing
        raw_input("press enter to close")
        
print "Closing..."        
sys.exit()                                                      # Closes the program
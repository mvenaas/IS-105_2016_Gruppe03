from socket import *
import sys
import select

address = ('localhost', 6005)                                   # The adress which the client need to connect to, to establish the connection
server_socket = socket(AF_INET, SOCK_DGRAM)                     # Establish the socket
server_socket.bind(address)                                     # Binds the socket and adress, which keeps an connection open to the user client
connected = False                                               # An boolean check. False by default, but changes to True when there is an connection
# print "Server is now awaiting the client, please connect"     # We do not use this right now, since we use the server program within RiverCrossing program

while(connected == False):                                      # While connected == False, the server will listen
    recv_data, addr = server_socket.recvfrom(2048)
    # print recv_data                                           # We do not need to print the request number now, we only want to confirm that an connection was made
    
    # Below we check the data we recieve from the client, and depending on the information given 
    # two possible outcomes may occure
    if recv_data == "Connected" :
        connected = True
        print "Server / client established connection"
        data = "Connected"
        server_socket.sendto("Connected", addr)
        
    elif recv_data == "Request 2" :
        connected = True
        print "Server / client established connection"
        data = "Connected"
        server_socket.sendto(data, addr)
        
       

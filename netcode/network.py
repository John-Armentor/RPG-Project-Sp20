#Author:    John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:  2020 02 10
#Course:    CSC424 - Software Engineering II
#Modified:  2020 03 04
#Course:    CSC425 - Software Engineering II
#Prof:      Dr. A. Louise Perkins

# File for the object that acts as the network for our game.  Allows the
# sending of serialized objects to the server as well as for obtaining the player's ID

import socket
import pickle
from settings import *


# The class we initialize to interact with the server
#
class Network:
    def __init__(self):
    
        # We establish a socket with the type of connection will will be using.
        # We establish a socket with the type of connection will will be using.
        # AF_INET showing that we are using IPv4 and SOCK_STREAM showing
        # it is a TCP socket
        #
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # The server IP we will pull from our settings.py file
        #
        self.server = LOCALHOST
        
        # a good, typically open port, but can be changed as needed
        #
        self.port = 5555
        
        # we create our address 
        #
        self.address = (self.server, self.port)
        
        # we store the initial data recieved from out connection
        #
        self.initial_data = self.connect()
    
    # Function to return the initial data from our connection
    #
    def get_initial_data(self):
        return self.initial_data

    # our function to attempt to connect to the server 
    #
    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(1024*4))
        except:
            pass

    # we create a send data function that uses pickling to serialize objects and send data as needed
    #
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(1024*4))
        except socket.error:
            print(socket.error)
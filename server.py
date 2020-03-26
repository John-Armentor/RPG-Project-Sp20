#Author:    John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:      2020 02 10
#Course:    CSC424 - Software Engineering II
#Modified:      2020 03 05
#Course:    CSC425 - Software Engineering II
#Prof:      Dr. A. Louise Perkins

# File that acts as the server for our game.  Intended to be launchable by
# anyone looking to host.

import sys
sys.path.append('./player_character/')
sys.path.append('./player_character/abilities')
sys.path.append('./player_character/skills')
sys.path.append('./game_items')
sys.path.append('./game_engine')
sys.path.append('./netcode/')

import player_character
import character_creation
import abilities
import skills
import game_item
import game_item_actions
import user
import tabletop
import main_menu
import chat_message
import dice

import tkinter
import uuid
from functools import partial

from FunctionPackager import FunctionPackager
import socket
import pickle
import multiprocessing
from _thread import *
from network import Network
from settings import *
import time

# queue of functions that are incoming from players and applying to the current game table
#
master_function_queue = multiprocessing.Queue()

# we initialize a game table and GM serverside
#
gm1 = user.User()
gm1.is_gamemaster = True
gm1.active_character = player_character.PlayerCharacter()
gm1.active_character.name = "Gamemaster"
                
table1 = tabletop.Tabletop(gm1)

# the test function from client to demonstrate we can pass functions from client to server and 
# execute them here
#
def TestFunction(first_word, second_word):
    print(first_word + " " + second_word)

# We create a function that acts as a threaded client
#
def threaded_client(connection):

    # we retrieve our global variables that are the master function queue and the game table
    #
    global master_function_queue
    global table1

    # we establish a connection to the client by sending the initial game table copy
    #
    connection.send(pickle.dumps(table1))
    while True:
        try:
            
            # we attempt to recieve 2048 bits of data that was pickled and we can increase the size of the data using the multiplier
            #
            inbound_data = pickle.loads(connection.recv(1024*4))
            print("Incoming: ", inbound_data)
            
            # we place the recieved fucntion in the master queue
            #
            master_function_queue.put(inbound_data)

            # this is to show that we are disconnecting and the break out once the client stops sending information and loses connection
            #
            if not inbound_data:
                print("Disconnected")
                break
                
            # else we send back the updated copy of the game table
            #            
            else:
                outbound_data = table1
                connection.sendall(pickle.dumps(outbound_data))
                print("Outgoing data sent")
                    
        except:
            break
            
    # To cover the case of the connection closing to prevent any infinite loops 
    #
    print("Lost connection")
    connection.close()

# this thread acts as our master thread for the server which will be the main game loop
# running on the server and process the master function queue onto the game table
#
def master_controller(x):
    global master_function_queue
    global table1
    
    while True:
        if not master_function_queue.empty():
            next_function = master_function_queue.get()
            next_function.execute_function()

# we initialize our master controller thread
#
start_new_thread(master_controller,(1,))

# We set a variable for the server the same as our local host setting in out settings.py file
#
server = LOCALHOST

# We set the port to 5555 as it is in a commonly unused port range to avoid the commonly used ones
#
port = 5555

# We now create a socket and use the settings to show that we are using TCP (SOCK_STREAM) and IPv4 (AF_INET)
#
current_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# a try except in the even that an error is thrown when we attempt to bind to the server and port
# useful if the port is in use
#
try:
    current_socket.bind((server, port))
except socket.error:
    str(socket.error)

# We listen for connections, this can accept an integer, limiting how many can connect to the server, this dictates the server size limit
#
current_socket.listen()
print("--Server Initialized--")
print("Listening for Connections...")

# we create a loop that constantly checks for new connections to be accepted and establishes a threaded client connection
#
while True:
    connection, address = current_socket.accept()
    print("Connected established with:", address)
    start_new_thread(threaded_client, (connection,))
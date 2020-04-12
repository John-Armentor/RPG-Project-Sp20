#Author:    John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:  2020 03 09
#Course:    CSC425 - Software Engineering II
#Prof:      Dr. A. Louise Perkins

# Main game method of our project.

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

from network import *
import multiprocessing
from _thread import *
from FunctionPackager import FunctionPackager
import time
import os


# queue of functions that are outgoing from the player to the server
#
client_function_queue = multiprocessing.Queue()

# Multiplayer settings
#
ISHOST = False
LOCALHOST = ""

def setIP():
    global LOCALHOST
    global ISHOST

    selection = int(input("Enter 1 to host or 2 to join a server: "))
    
    if selection == 1:
        ISHOST = True
        LOCALHOST = socket.gethostbyname(socket.gethostname())
        
    else:
        ISHOST = False
        LOCALHOST = input("enter an IPv4 address: ")

# acts as a function for the sake of demonstrating that one can
# be passed from client all the way to the master thread in the
# server
#
def TestFunction(first_word, second_word):
    print(first_word + " " + second_word)

# acts as the master thread for the client that will process all of the data
# in the client function queue and send it off to the server, while recieving abilities
# updated copy of the gameboard back each time
#
def client_master_controller(current_network):
    global client_function_queue
    global table1
    
    while True:
        if not client_function_queue.empty():
            next_function_to_send = client_function_queue.get()
            table1 = current_network.send(next_function_to_send)
            

# the function that will be used to have a function sent to the server
# within the main game loop
#
def send_to_server(function, args):
    function_to_send = FunctionPackager(function, args)
    client_function_queue.put(function_to_send)


# definition of Main
#
def main():
    
    # Set run to true to keep the game looping
    #
    run = True
    
    setIP()
    
    if ISHOST:
        os.system("start cmd /c server.py")
        print("Server Launching...")
        time.sleep(3)
    
    # We initialize a network object to communicate with the server
    #
    current_network = Network(LOCALHOST)
    
    # our client side copy of the server's game table
    #
    table1 = current_network.get_initial_data()
    
    # we initialize our master controller thread
    #
    start_new_thread(client_master_controller,(current_network,))
    

    # Main Game Loop
    #
    while run:
        words = str(input("Say something..."))
        send_to_server(print,(words))
        
main()
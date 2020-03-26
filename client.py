#Author:    John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:  2020 03 05
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

from network import Network
from FunctionPackager import FunctionPackager
import time

# acts as a function for the sake of demonstrating that one can
# be passed from client all the way to the master thread in the
# server
#
def TestFunction(first_word, second_word):
    print(first_word + " " + second_word)

# definition of Main
#
def main():

    # Set run to true to keep the game looping
    #
    run = True
    
    # We initialize a network object to communicate with the server
    #
    current_network = Network()
    
    # our client side copy of the server's game table
    #
    table1 = current_network.get_initial_data()
    

    # Main Game Loop
    #
    while run:
    
        # we demonstrate how to package a function
        #
        func = TestFunction
        args = ("testing", "testing")
        function_to_send = FunctionPackager(func, args)
        
        # the send method both sends our function and recieves an updated 
        # copy of the game table from the server
        #
        table1 = current_network.send(function_to_send)
        
        # a way to control server update cycles
        #
        time.sleep(.5)
        
main()
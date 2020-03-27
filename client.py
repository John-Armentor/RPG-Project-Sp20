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

import rpyc
import socket
import time
import os


# Multiplayer settings
#
ISHOST = False
HOSTIP = ""

def setIP():
    global HOSTIP
    global ISHOST

    selection = int(input("Enter 1 to host or 2 to join a server: "))
    
    if selection == 1:
        ISHOST = True
        HOSTIP = socket.gethostbyname(socket.gethostname())
        print("You are now hosting. Your IP is: " + HOSTIP)
        
    else:
        ISHOST = False
        HOSTIP = input("enter an IPv4 address: ")


# definition of Main
#
def main():
    
    # Set run to true to keep the game looping
    #
    run = True
    
    setIP()
    
    if ISHOST:
        os.system("start cmd /c rpyc_classic.py --host 0.0.0.0")
        print("Server Launching...")
        time.sleep(3)
        
        print("Initializing Table...")
        campaign_title = "The Chronicles of Testing"
        gm1 = user.User(True)
        host_table = tabletop.Tabletop(gm1, campaign_title)
    
    conn = rpyc.classic.connect(HOSTIP)
    hostspace = conn.modules.sys

    # Main Game Loop
    #
    while run:
        words = input("Say something...")
        
main()
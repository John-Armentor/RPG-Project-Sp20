#Author:    Jacob Horst
#Email:     jacob.horst@usm.edu
#Date:      03/17/2020
#Course:    CSC424 - Software Engineering II
#Prof.:     Dr. A. Louise Perkins

import player_character
import tkinter
import sys
sys.path.append('./player_character/abilities')
import abilities
sys.path.append('./player_character/skills')
import skills


###################################
#### Character Sheet Screen ####
###################################
def character_sheet(f_character):

    print("Character Sheet:")
    print()
    
    # tkinter window for GUI character sheet
    character_sheet_window = tkinter.Tk()           
    character_sheet_window.title("Character Sheet")

    ############ Player Information ############

    # Uses the player_character.py build_frame func to display the character info
    # Includes name, description, and ability values 
    player_info_frame = f_character.build_frame(character_sheet_window)
    player_info_frame.grid(row = 0, column = 0, sticky = tkinter.N)

    # Displays the character's current skill values



    # Displays the character's current hitpoints



    # Displays the character's currently wielded items



    # Button to enable the player to view their inventory



    # Button to enable the player to create a character




    character_sheet_window.mainloop()
    # End character sheet window
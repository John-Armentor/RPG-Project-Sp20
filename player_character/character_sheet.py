#Author:    Jacob Horst
#Email:     jacob.horst@usm.edu
#Date:      03/17/2020
#Course:    CSC424 - Software Engineering II
#Prof.:     Dr. A. Louise Perkins

import player_character
import character_creation
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
    player_info_frame.grid(row = 0, column = 0, sticky = tkinter.N, padx = 5, pady = 5)

    # Displays the character's current skill values



    # Displays the character's current hitpoints
    hitpoint_frame = tkinter.LabelFrame(character_sheet_window, text = "Hitpoints", 
                                        labelanchor = tkinter.N)
    hitpoint_frame.grid(row = 0, column = 1, sticky = tkinter.N, padx = 5, pady = 5)

    for each_hitbox in f_character.max_hitpoints:  
            hitpoint_string = (str(each_hitbox) + ": " +
                               str(f_character.current_hitpoints[each_hitbox]) +
                               "/" +
                               str(f_character.max_hitpoints[each_hitbox]) )
            
            hitpoint_label = tkinter.Label(hitpoint_frame, text = hitpoint_string)
            hitpoint_label.pack()


    # Displays the character's currently wielded items
    wielded_item_frame = tkinter.LabelFrame(character_sheet_window, text = "Wielded Items",
                                            labelanchor = tkinter.N)
    wielded_item_frame.grid(row = 0, column = 2, sticky = tkinter.N, padx = 5, pady = 5)

    for each_item in f_character.item_slots:
            item_string = (str(each_item) + ":\t" + str(f_character.item_slots[each_item]))

            item_label = tkinter.Label(wielded_item_frame, text = item_string)
            item_label.pack()


    # Function for inventory button, opens a window that displays the player's current inventory
    def view_inventory():
        inventory_window = tkinter.Tk()           
        inventory_window.title("Inventory")

        for each_item in player1.item_slots:
            inventory_string = (str(each_item) + ":\t" + str(f_character.item_slots[each_item]))

            inventory_label = tkinter.Label(inventory_window, text = inventory_string)
            inventory_label.pack()

        view_inventory.mainLoop()
        # End inventory window

    # Button to enable the player to view their inventory
    inventory_button = tkinter.Button(character_sheet_window, text = "Inventory",
                                      command = view_inventory)
    inventory_button.grid(row = 1, column = 1, padx = 10, pady = 10)


    # Function for character creation button, opens the character creation window
    def enter_character_creation():
        character_creation.character_creation(f_character)

    # Button to enable the player to create a character
    character_creation_button = tkinter.Button(character_sheet_window, text = "Create a Character",
                                               command = enter_character_creation)
    character_creation_button.grid(row = 2, column = 1, padx = 10, pady = 10)



    character_sheet_window.mainloop()
    # End character sheet window
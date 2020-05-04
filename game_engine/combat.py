#Author:    Jacob Horst
#Email:     jacob.horst@usm.edu
#Date:      04/19/2020
#Course:    CSC424 - Software Engineering II
#Prof.:     Dr. A. Louise Perkins

"""
    This file contain function definitions for commands
        used to facilitate combat rounds and turns
"""

import dice
import chat_message
import sys
sys.path.append('./player_character/')
sys.path.append('./player_character/abilities')
sys.path.append('./player_character/skills')
sys.path.append('./game_items')
sys.path.append('./story_items')

import player_character
import abilities
import skills
import game_item
import game_item_actions
import tabletop
import chat_message
import story_item
import tkinter
from PIL import Image, ImageTk #image handling for various file types


###################################
#######   Combat Screen   #########
###################################
def combat(parent_window, f_game_table, f_character):

    print("Combat")
    print()

    # tkinter window for combat GUI
    combat_window = tkinter.Toplevel(parent_window)           
    combat_window.title("Combat")
    combat_window.state('zoomed')



    ##### CHAT ##### 

    #refresh the chatlog
    def refresh_chatlog():
        for each_message in chatlog_frame.winfo_children():
            each_message.destroy()

        for each_message in f_game_table.chatlog.values():
            #build frame from class
            this_message = f_game_table.chatlog[each_message.object_id].build_frame(chatlog_frame)      
            this_message.pack()

        combat_window.after(250, refresh_chatlog)   #refresh 4 times per second
    #end refresh chatlog

    #controller for chat entry send button
    def send_chat_message():
        if (len(chat_entry.get()) > 0):
            msg = chat_message.ChatMessage(f_character, 
                                           "speech", "public", 
                                           chat_entry.get())
            f_game_table.put_on_table(msg)
            f_game_table.chatlog[msg.object_id].print_chat_message()  #debugging
        chat_entry.delete(0, "end")        #clear the entry field
        #self.refresh_chatlog()


    #build frame
    chatlog_frame = tkinter.LabelFrame(combat_window, text = "Chatlog:", padx = 5, pady = 5,
                                       labelanchor = tkinter.NW)
    chatlog_frame.grid(row = 0, column = 0, rowspan = 6, sticky = tkinter.N)
    refresh_chatlog() #keep up to date

    for each_message in f_game_table.chatlog.values():
        #build frame from class
        this_message = f_game_table.chatlog[each_message.object_id].build_frame(chatlog_frame)      
        this_message.pack()
    #end populate chatlog

    #text entry to create chat message
    chat_entry = tkinter.Entry(combat_window)     #text entry field
    chat_entry.grid(row = 6, column = 0, sticky = tkinter.N)


    chat_submit = tkinter.Button(combat_window, text = "Send", command = send_chat_message)
    chat_submit.grid(row = 7, column = 0, sticky = tkinter.N)
    #end text entry chat message

    ##### END CHAT #####



    ##### PLAYER INFO #####

    # frame to hold player information
    player_info_frame = tkinter.LabelFrame(combat_window, text = f_character.name, padx = 5, pady = 5,
                                           labelanchor = tkinter.NW)
    player_info_frame.grid(row = 0, column = 1, rowspan = 2, sticky = tkinter.N)

    #if image exists, load it and pack it
    if(f_character.image_filename != ""):
        image = Image.open(f_character.image_filename)
        image.thumbnail((400,400), Image.ANTIALIAS) 
        tk_image = ImageTk.PhotoImage(image)
        frame_image = tkinter.Label(player_info_frame, image=tk_image)
        frame_image.image = tk_image
        frame_image.pack()

    #refresh hitpoints
    def refresh_hitpoints():
        for each_label in hitpoint_frame.winfo_children():
            each_label.destroy()
        
        for each_hitbox in f_character.max_hitpoints:  
            hitpoint_string = (str(each_hitbox) + ": " +
                               str(f_character.current_hitpoints[each_hitbox]) +
                               "/" +
                               str(f_character.max_hitpoints[each_hitbox]) )
            
            hitpoint_label = tkinter.Label(hitpoint_frame, text = hitpoint_string)
            
            #format to highlight damage
            if (f_character.current_hitpoints[each_hitbox] < 0):
                hitpoint_label.config(foreground = "red")
            elif (f_character.current_hitpoints[each_hitbox] <
                f_character.max_hitpoints[each_hitbox]):
                hitpoint_label.config(foreground = "orange")

            hitpoint_label.pack()
        
        combat_window.after(250, refresh_hitpoints)   #refresh 4 times per second (250 ms)
    #end refresh hitpoints

    # frame to display current HP
    hitpoint_frame = tkinter.LabelFrame(player_info_frame, text = "Hitpoints:", padx = 5, pady = 5,
                                        labelanchor = tkinter.NW)
    hitpoint_frame.pack()
    refresh_hitpoints()

    #get hitpoint maximums from player's character
    for each_hitbox in f_character.max_hitpoints:  
        hitpoint_string = (str(each_hitbox) + ": " +
                           str(f_character.current_hitpoints[each_hitbox]) +
                           "/" +
                           str(f_character.max_hitpoints[each_hitbox]) )
            
        hitpoint_label = tkinter.Label(hitpoint_frame, text = hitpoint_string)
            
        #format to highlight damage
        if (f_character.current_hitpoints[each_hitbox] < 0):
            hitpoint_label.config(foreground = "red")
        elif (f_character.current_hitpoints[each_hitbox] <
              f_character.max_hitpoints[each_hitbox]):
              hitpoint_label.config(foreground = "orange")

        hitpoint_label.pack()

        ##### END PLAYER INFO #####



    ##### ACTIONS  #####

    # Temp label to show design for 'actions remaining'
    actions_remaining_label = tkinter.Label(combat_window, text = "Actions Remaining: 3")
    actions_remaining_label.grid(row = 2, column = 1)

    # List of possible actions for the player and list of possible targets
    action_list = ["Attack"]
    target_list = ["Target 1", "Target 2", "Target 3"]
    action_var = tkinter.StringVar(value = action_list)
    target_var = tkinter.StringVar(value = target_list)

    # Listboxes used to display available actions and targets
    action_label = tkinter.Label(combat_window, text = "Actions:")
    action_label.grid(row = 3, column = 1)
    action_listbox = tkinter.Listbox(combat_window, height = 1, listvariable = action_var)
    action_listbox.grid(row = 4, column = 1)

    target_label = tkinter.Label(combat_window, text = "Targets:")
    target_label.grid(row = 5, column = 1)
    target_listbox = tkinter.Listbox(combat_window, height = 1, listvariable = target_var)
    target_listbox.grid(row = 6, column = 1)

    action_var.set(action_list)
    target_var.set(target_list)

    # Button to perform selected action
    perform_action_button = tkinter.Button(combat_window, text = "Perform Action")
    perform_action_button.grid(row = 7, column = 1, padx = 10, pady = 10,
                                   sticky = tkinter.N)

    ##### END ACTIONS #####



    ##### TARGETS #####

    #refresh npc hitpoints
    def refresh_npc_hitpoints(npc):
        for each_label in npc_hitpoint_frame.winfo_children():
            each_label.destroy()
        
        for each_hitbox in npc.max_hitpoints:  
            hitpoint_string = (str(each_hitbox) + ": " +
                               str(npc.current_hitpoints[each_hitbox]) +
                               "/" +
                               str(npc.max_hitpoints[each_hitbox]) )
            
            hitpoint_label = tkinter.Label(hitpoint_frame, text = hitpoint_string)
            
            #format to highlight damage
            if (npc.current_hitpoints[each_hitbox] < 0):
                hitpoint_label.config(foreground = "red")
            elif (npc.current_hitpoints[each_hitbox] <
                npc.max_hitpoints[each_hitbox]):
                hitpoint_label.config(foreground = "orange")

            hitpoint_label.pack()
        
        combat_window.after(250, refresh_npc_hitpoints)   #refresh 4 times per second (250 ms)
    #end refresh hitpoints

    # frame to hold list of targets and target information
    target_frame = tkinter.LabelFrame(combat_window, text = "Targets:", padx = 5, pady = 5,
                                      labelanchor = tkinter.NW)
    target_frame.grid(row = 0, column = 2, rowspan = 8, sticky = tkinter.N)

    # debugging
    test_label = tkinter.Label(target_frame, text = "This is the target frame")
    test_label.pack()

    # creates frame and displays information for each npc in tabletop.nonplayer_characters
    for each_npc in f_game_table.nonplayer_characters.values():
        npc_frame = tkinter.LabelFrame(target_frame, 
                                      text = f_game_table.nonplayer_characters[each_npc.object_id].name,
                                      padx = 5, pady = 5, labelanchor = tkinter.NW)
        npc_frame.grid(rowspan = 2, sticky = tkinter.N)

        # debugging
        test_label2 = tkinter.Label(npc_frame, text = "This is the npc frame")
        test_label2.pack()

        # if image exists, load it and pack it
        if(f_game_table.nonplayer_characters[each_npc.object_id].image_filename != ""):
            image = Image.open(f_game_table.nonplayer_characters[each_npc.object_id].image_filename)
            image.thumbnail((400,400), Image.ANTIALIAS) 
            tk_image = ImageTk.PhotoImage(image)
            frame_image = tkinter.Label(npc_frame, image=tk_image)
            frame_image.image = tk_image
            frame_image.pack()


        # frame to display current HP
        npc_hitpoint_frame = tkinter.LabelFrame(npc_frame, text = "Hitpoints:", padx = 5, pady = 5,
                                        labelanchor = tkinter.NW)
        npc_hitpoint_frame.pack()
        refresh_npc_hitpoints(f_game_table.nonplayer_characters[each_npc.object_id])

        #get hitpoint maximums from player's character
        for each_hitbox in f_game_table.nonplayer_characters[each_npc.object_id].max_hitpoints:  
            hitpoint_string = (str(each_hitbox) + ": " +
                            str(f_game_table.nonplayer_characters[each_npc.object_id].current_hitpoints[each_hitbox]) +
                            "/" +
                            str(f_game_table.nonplayer_characters[each_npc.object_id].max_hitpoints[each_hitbox]) )
            
            hitpoint_label = tkinter.Label(npc_hitpoint_frame, text = hitpoint_string)
            
            #format to highlight damage
            if (f_game_table.nonplayer_characters[each_npc.object_id].current_hitpoints[each_hitbox] < 0):
                hitpoint_label.config(foreground = "red")
            elif (f_game_table.nonplayer_characters[each_npc.object_id].current_hitpoints[each_hitbox] <
                f_game_table.nonplayer_characters[each_npc.object_id].max_hitpoints[each_hitbox]):
                hitpoint_label.config(foreground = "orange")

            hitpoint_label.pack()

    combat_window.mainloop()
    # End combat window






def attack_action(f_table, f_attacker, f_defender, 
                  f_attacker_skill = "unarmed", f_defender_skill = "unarmed", 
                  f_attacker_difficulty = "standard", f_defender_difficulty = "standard",
                  f_attacker_weapon = "unarmed", f_defender_weapon = "unarmed"):


    chat_msg = str("attacks " + str(f_defender.first_name) + ". ")

    #initialize parameter of unarmed to character's game item
    if (f_attacker_weapon == "unarmed"):
        f_attacker_weapon = f_attacker.unarmed
    if (f_defender_weapon == "unarmed"):
        f_defender_weapon = f_defender.unarmed #here would be a defender's shield if they had one.


    #attempt opposed combat skill check between attacker and defender
    try:
        skill_results = dice.opposed_check(f_table, f_attacker, f_defender, 
                                           f_attacker_skill, f_attacker_difficulty,
                                           f_defender_skill, f_defender_difficulty)
    
    except Exception as error:
        print("An error occurred in attack_action when making the skill check:")
        print(error)
        print("Parameters:")
        print(locals(), sep="\n")

    else:
        if (skill_results[0] == None): #if no-ne succeeds the attack or parry roll
            print("attack_action: No one succeeded their combat roll.") #debugging
            chat_msg = chat_msg + "Both failed their combat maneuvers. "

        elif (skill_results[0] == f_attacker): #attacker wins
            print("attack_action: The attack roll was successful.") #debugging
            chat_msg = chat_msg + "The attack succeeds! "

            try: #perform attack action
                f_attacker_weapon.actions["weapon_attack"](f_attacker_weapon, 
                                                         f_attacker, f_defender,
                                                         skill_results[1])
            except Exception as error:
                print("An error occurred in combat.py > attack_action, " +
                      "while attempting weapon_attack:")
                print(error)
                print("Parameters:")
                print(locals(), sep="\n")


        else: #defender wins
            print("attack_action: The defender parried.") #debugging
            chat_msg = chat_msg + str(f_defender.first_name) + " parried the attack!"

    f_table.put_on_table(chat_message.ChatMessage(f_attacker, "action", "public", chat_msg))
#end attack_action()

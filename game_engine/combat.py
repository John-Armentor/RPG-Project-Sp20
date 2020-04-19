#Author:    Jacob Horst
#Email:     jacob.horst@usm.edu
#Date:      04/19/2020
#Course:    CSC424 - Software Engineering II
#Prof.:     Dr. A. Louise Perkins

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

###################################
#######   Combat Screen   #########
###################################
def combat(f_game_table, f_user):

    print("Combat")
    print()

    # tkinter window for combat GUI
    combat_window = tkinter.Toplevel()           
    combat_window.title("Combat")



    ##### CHAT ##### 
    #build frame
    chatlog_frame = tkinter.LabelFrame(combat_window, text = "Chatlog:", padx = 5, pady = 5)
    chatlog_frame.grid(row = 0, column = 0)
    refresh_chatlog() #keep up to date

    for each_message in f_game_table.chatlog.values():
        #build frame from class
        this_message = f_game_table.chatlog[each_message.object_id].build_frame(chatlog_frame)      
        this_message.pack()
    #end populate chatlog

    #text entry to create chat message
    chat_entry = tkinter.Entry(combat_window)     #text entry field
    chat_entry.grid(row = 1, column = 0)


    chat_submit = tkinter.Button(combat_window, text = "Send", command = send_chat_message)
    chat_submit.grid(row = 2, column = 0)
    #end text entry chat message

    ##### END CHAT #####



    #controller for chat entry send button
    def send_chat_message():
        if (len(chat_entry.get()) > 0):
            msg = chat_message.ChatMessage(f_user.active_character, 
                                           "speech", "public", 
                                           chat_entry.get())
            f_game_table.put_on_table(msg)
            f_game_table.chatlog[msg.object_id].print_chat_message()  #debugging
        chat_entry.delete(0, "end")        #clear the entry field
        #self.refresh_chatlog()
    #



    #refresh the chatlog
    def refresh_chatlog():
        for each_message in chatlog_frame.winfo_children():
            each_message.destroy()

        for each_message in f_game_table.chatlog.values():
            #build frame from class
            this_message = f_game_table.chatlog[each_message.object_id].build_frame(chatlog_frame)      
            this_message.pack()

        combat.after(250, refresh_chatlog)   #refresh 4 times per second
    #end refresh chatlog

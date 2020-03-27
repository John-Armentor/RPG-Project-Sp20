#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 12
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the class definition for a chat message,
#   to be sent between players by players and appear in the 
#   chat log in the main GUI.
#
#   A "message" includes not just the string of the message but also:
#       the speech type (spoken word, action description, etc) 
#       the UUIDs (.object_id) of the speaker and of all receipiants 
#           for whom the message is visible
#       the visibility type (public, whisper, etc)
#       the language in which the message was spoken
#       and linked game objects in the message (trunk)

import uuid
import tkinter

class ChatMessage:

    def __init__(self, f_speaker, f_type, f_visibility, 
                 f_message = "", f_language = "", f_objects = None): 
        self.object_id = uuid.uuid1()
        self.table = None   #set by tabletop.py put_on_table()

        #speaker is a PlayerCharacter object for player users
        #   is a User object for gamemaster
        #   in both cases speaker is the whole object, not just the name
        #   this is to allow access to the speakers object_id if needed
        self.speaker = f_speaker

        self.type = f_type
        self.visibility = f_visibility

        self.message = f_message
        self.language = f_language

        self.trunk = {}
        if f_objects != None:
            for each_object in f_objects:
                self.trunk[each_object.object_id] = each_object
    #end initializer



    #print message to console for testing and debugging
    def print_chat_message(self):
        print("Chat Message:\n" +
              "ID:\t" + str(self.object_id) + "\n" +
              "Speaker:\t" + str(self.speaker.name) + " (" + str(self.speaker.object_id) + ")\n" +
              "Type:\t" + str(self.type) + "\tVisibility:\t" + str(self.visibility) + "\n" +
              "Message:\t" + str(self.message) +
              "")
        if (self.language != ""):
            print("Language:\t" + str(self.language))
        for each_object in self.trunk.values():
            print(str(each_object.name))
    #end print message




    #frame builder method to place a message into a tkinter window
    #build a tkinter formatted frame from item attributes
    def build_frame(self, f_window):
        frame = tkinter.LabelFrame(f_window, text = self.speaker.name)

        #determine font color based off message type
        if (self.type == "speech"):        
            formatted_text = (str(self.speaker.first_name) + " says:\n" +
                              str(self.message))
            formatted_color = "green"

        elif (self.type == "action"):
            formatted_text = (str(self.speaker.name) + " " + 
                              str(self.message))
            formatted_color = "red"

        elif (self.type == "technical"):
            formatted_text = (str(self.message))
            formatted_color = "black"

        elif (self.type == "die_roll"):
            None #TODO

        frame_message = tkinter.Label(frame, text = formatted_text, foreground = formatted_color)
        frame_message.pack()

        return frame
    #


    #open the frame in a window for testing purposes
    def open_frame(self):
        frame_window = tkinter.Tk()
        tkinter_frame = self.build_frame(frame_window)

        frame_window.title(self.speaker)
        frame_window.geometry("400x600")

        tkinter_frame.pack()

        frame_window.mainloop()
    #


#end clas chat message
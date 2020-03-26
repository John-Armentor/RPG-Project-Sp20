#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 03 01
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the story item class.
#   a story item is a text entity made by the GM in preperation
#   to share with the players. It can be shared in the chatlog and 
#   kept open in a special section of the main window so that it 
#   remains visible to the players.

import uuid
import tkinter
from PIL import Image, ImageTk #image handling for various file types

class StoryItem():
    def __init__(self):
        self.object_id = uuid.uuid1()
        self.table = None   #set by tabletop.py put_on_table()
        self.title = ""
        self.message = ""
        self.next_item = None   #can store another story_item
        self.image_filename = ""       #stores a system path to a picture
        self.trunk = {}         #stores any other objects as needed

        #self.tkinter_frame = None  #outdated, use build_frame() instead 

    #end initializer
    


    #build a tkinter formatted frame from item attributes
    def build_frame(self, f_window):
        frame = tkinter.LabelFrame(f_window, text = self.title)

        frame_message = tkinter.Label(frame, text = self.message)
        frame_message.pack()
        
        #if image exists, load it and pack it
        if(self.image_filename != ""):
            image = Image.open(self.image_filename)
            image.thumbnail((400,400), Image.ANTIALIAS) #resize to fit in window, TODO: update to resize automatically
            tk_image = ImageTk.PhotoImage(image)
            frame_image = tkinter.Label(frame, image=tk_image)
            frame_image.image = tk_image
            frame_image.pack()

            #TODO: in a future implementation:
            #   add next_item and trunk


        return frame
    #

    #open the frame in a window for testing purposes
    def open_frame(self):
        frame_window = tkinter.Tk()
        tkinter_frame = self.build_frame(frame_window)

        frame_window.title(self.title)
        frame_window.geometry("400x600")

        tkinter_frame.pack()

        frame_window.mainloop()
    #

#end story item class
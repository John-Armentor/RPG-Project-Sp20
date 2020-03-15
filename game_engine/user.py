#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 14
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This class defines a player object 
#   (the human user as opposed to the virtual character)
#   it contains whether the user is a game master,
#   any characters they control,
#   their IP address,
#   etd

import socket    
import uuid

class User:
    def __init__(self, f_is_gamemaster = False, 
                 f_character = None): 
        self.object_id = uuid.uuid1()
        self.table = None   #set by tabletop.py put_on_table()
        self.ip_address = socket.gethostbyname(socket.gethostname())
        self.is_gamemaster = f_is_gamemaster

        #create dependancies for chat message object
        #   required for chat messages spoken by gm
        if f_is_gamemaster:
            self.name = "Gamemaster"
            self.first_name = "Gamemaster"
            self.last_name = "Gamemaster"

        self.character = []
        if (f_character != None):
            self.character.append(f_character)
            self.active_character = self.character[0]
        else:
            self.active_character = None
    #end initializer
#end player class


#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 14
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This class defines a player object 
#   (the human user as opposed to the virtual character)
#   it contains whether the user is a game master,
#   any characters they control,
#   their IP address,
#   etd

import socket    
import uuid

class Player:
    def __init__(self, f_is_gamemaster = False, 
                 f_character = None): 
        self.object_id = uuid.uuid1()
        self.ip_address = socket.gethostbyname(socket.gethostname())
        self.is_gamemaster = f_is_gamemaster

        self.character = []
        if (f_character != None):
            self.character.append(f_character)
            self.active_character = self.character[0]
        else:
            self.active_character = None
    #end initializer
#end player class


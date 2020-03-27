#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 11
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This class will act as the game state of a game station. 
#   "tabletop" refers to the game objects that are "in play",
#   and should be able to be refered to from anywhere in the program.
#
#   It will hold things like the players that are connected to 
#       the session and their characters, and any objects the 
#       Game Master (GM) wants to present to the players.

import sys
sys.path.append('./player_character/')
sys.path.append('./player_character/abilities')
sys.path.append('./player_character/skills')
sys.path.append('./game_items')

import player_character
import abilities
import skills
import species
import game_item
import game_item_actions
import chat_message

import tkinter
import uuid

#tabletop contains:
#   player characters
#   non player characters
#   game items

class Tabletop:
    def __init__(self, f_gamemaster, f_campaign_name = "Campaign"):
        self.object_id = uuid.uuid1()
        self.gamemaster = f_gamemaster     #stores unique identifier of game master (GM)
        self.campaign_name = f_campaign_name

        self.users = {}
        
        #store characters
        self.player_characters = {}         #controlled by players (remote users)
        self.nonplayer_characters = {}      #controlled by GM
        
        #store game items
        self.game_items = {}

        #store story items
        self.story_items = {}

        #store chatlog messages
        self.chatlog = {}
        #populate chatlog (initializes with welcome message)
        self.put_on_table(chat_message.ChatMessage(self.gamemaster, 
                                                   "technical", "public", 
                                                   "Welcome to Chatquest RPG!"))

        #store anything that doesn't match a predefined class,
        #   used when put_on_table can't find the object's class type
        self.trunk = {}


        #load skills and abilities, can be modified per campaign by GM (future implementation)
        self.skills = skills.default_skills
        self.abilities = abilities.default_abilities

        #species
        self.species = species.default_species_list

    #end initializer
    
       
    #auto add to table function, determines the class type and stores in proper dictionary
    def put_on_table(self, f_token):
        if f_token.__class__.__name__ == "PlayerCharacter":
            self.player_characters[f_token.object_id] = f_token

        elif f_token.__class__.__name__ == "NonplayerCharacter":
            self.nonplayer_characters[f_token.object_id] = f_token

        elif f_token.__class__.__name__ == "GameItem":
            self.game_items[f_token.object_id] = f_token

        elif f_token.__class__.__name__ == "ChatMessage":
            self.chatlog[f_token.object_id] = f_token

        elif f_token.__class__.__name__ == "User":
            self.users[f_token.object_id] = f_token

        elif f_token.__class__.__name__ == "StoryItem":
            self.story_items[f_token.object_id] = f_token

        else:
            self.trunk[f_token.object_id] = f_token

        #set table attribute of token if it exists
        f_token.table = self

    #


    #print object IDs
    def print_object_ids(self):
        #get each attribute of the table
        for each_attribute in self.__dict__.values():

            #print(each_attribute.__name__)
            print(str(each_attribute.__class__.__name__))

            if (type(each_attribute) == dict):  #if its a dictionary
                for each_token in each_attribute.values():

                    print(str(each_token.__class__.__name__))

                    if (hasattr(each_token, "object_id")):  #if it has an object id
                        print(str(each_token.object_id))

            else:   #if not a dictionary
                print(str(each_attribute))

    #end print object IDs

#end tabletop class

#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 02
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#this file contains species playable by player characters

import random

class species: 
    def __init__(self, f_name):
        self.name = f_name

        #possible target zones, 
        #   dictionary with string key value for each tragetable body part
        #   paired with a percentage (1 to 100) representing the odds that 
        #   that area is hit. This would typically coorespond to the size
        #   of the area, so it also represents a portion of the hit points
        #   that area contains
        self.hitboxes = {}

        #item slots
        #   items held or worn by a character can be stored here
        self.item_slots = {}

        self.native_languages = []

    #end initializer


    def get_random_hitbox(self):
        """
            selects a random hitbox from the species hitbox dict,
            useful for dealing damage anytime the attacker does
            not target a location,
        """
        roll = random.randrange(100) #produces a pseudorandom integer between 0 and 99 inclusively
        i = 0
        for each_hitbox in self.hitboxes:
            i += self.hitboxes[each_hitbox]
            if roll < i:
                return each_hitbox
    #end return random hitbox


#end species definition

#list of all species
default_species_list = {}

#list of all languages
languages = {"vernacular": "vernacular"}

#the human species
human = species("human")
#hitbox values represent the percentage (1-100) of hp that hitbox takes,
#   and the probability that that hitbox gets hit in an attack,
#   MUST add up to 100
human.hitboxes["head"] = 10  
human.hitboxes["chest"] = 20
human.hitboxes["abdomen"] = 20
human.hitboxes["left_arm"] = 15
human.hitboxes["right_arm"] = 15
human.hitboxes["left_leg"] = 10
human.hitboxes["right_leg"] = 10

human.item_slots["head"] = None
human.item_slots["left_hand"] = None
human.item_slots["right_hand"] = None
human.item_slots["left_ring"] = None
human.item_slots["right_ring"] = None
human.item_slots["left_forearm"] = None
human.item_slots["right_forearm"] = None
human.item_slots["chest"] = None
human.item_slots["neck"] = None
human.item_slots["back"] = None
human.item_slots["feet"] = None
human.item_slots["waist"] = None
human.item_slots["legs"] = None

human.native_languages.append(languages["vernacular"])

default_species_list["human"] = human
#end human


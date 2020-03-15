#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 01 30
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the class and methods for initializing a 
#   player character game object.
#   
#   A player character (PC) is an entity controled by the remote users,
#       as opposed to the host user, that acts as the main protagonist of the game.
#   
#   A PC has several main statistics (Abilities) that it uses to 
#       affect its interactions with the game environement. 
#       These abilities indicate the character's prowess in feats
#       such as strength, agility, and the like.
#
#   A PC will also have an inventory of items it collects during the game.
#
#   Future implementation of this class will define methods to
#       engage in activities such as combat.

import tkinter
import species 
import sys
sys.path.append('./player_character/abilities')
import abilities
sys.path.append('./player_character/skills')
import skills
import uuid


#list of core ability scores
#abilities.coreAbilities.values() = ["strength", "constitution", "dexterity", "intelligence", "charisma"]






import character_creation


#player character class
class PlayerCharacter:

    def __init__(self, f_table):
        #demographics
        self.object_id = uuid.uuid1()
        self.table = f_table   #set by tabletop.py put_on_table()
        self.table.put_on_table(self)

        self.first_name = "NewGuy"
        self.middle_name = ""
        self.family_name = "McCharacter"
        self.name = str(self.first_name + " " + self.family_name)
        self.title = ""

        self.image_filename = ""       #stores a system path to a picture
        self.description = "A stunning Character."


        #add attributes from species
        self.species = self.table.species["human"]
        self.languages = self.species.native_languages
        self.item_slots = self.species.item_slots


        #abilities
        self.ability_scores = {}
        for each_ability in self.table.abilities.values():         #set each score to its minumum
            self.ability_scores[each_ability.id] = character_creation.min_ability_score

        #skill bases (sum of two linked abilities)
        self.skill_bases = {}
        for each_skill in self.table.skills.values():                #set each skill to the sum of its two linked abilities
            self.skill_bases[each_skill.id] = (self.ability_scores[each_skill.main_ability.id] + 
                                             self.ability_scores[each_skill.secondary_ability.id])

        #skill ranks (points added to skills at character chreation and level up)
        self.skill_ranks = {}
        for each_skill in self.table.skills.values():
            self.skill_ranks[each_skill.id] = 0

        #skill totals (sum of skill bases and skill ranks)
        self.skills = {}
        for each_skill in self.table.skills.values():
            self.skills[each_skill.id] = self.skill_bases[each_skill.id] + self.skill_ranks[each_skill.id]

        #combat stats
        self.speed = self.ability_scores["constitution"] * 2
        
        self.hitpoint_total = (self.ability_scores["size"] + self. ability_scores["constitution"]) * 2
        
        self.max_hitpoints = {}
        for each_hitbox in self.species.hitboxes:
            self.max_hitpoints[each_hitbox] = int(self.hitpoint_total * (self.species.hitboxes[each_hitbox]/100))

        self.current_hitpoints = {}
        for each_hitbox in self.species.hitboxes:
            self.current_hitpoints[each_hitbox] = self.max_hitpoints[each_hitbox]

        #inventory
        self.inventory = {}

    #end initializer



    #build frame
    #build a tkinter formatted frame from item attributes
    def build_frame(self, f_window):
        frame = tkinter.LabelFrame(f_window, text = self.name)

        frame_message = tkinter.Label(frame, text = self.description)
        frame_message.pack()
        
        #if image exists, load it and pack it
        if(self.image_filename != ""):
            image = Image.open(self.image_filename)
            image.thumbnail((400,400), Image.ANTIALIAS) #resize to fit in window, TODO: update to resize automatically
            tk_image = ImageTk.PhotoImage(image)
            frame_image = tkinter.Label(frame, image=tk_image)
            frame_image.image = tk_image
            frame_image.pack()
        #

        #abilities
        for each_ability in self.ability_scores:
            ability_string = str(str(self.table.abilities[each_ability].name) +
                                 ":\t" + str(self.ability_scores[each_ability]))
            ability_label = tkinter.Label(frame, text = ability_string)
            ability_label.pack()

        return frame
    #

    #open the frame in a window for testing purposes
    def open_frame(self):
        frame_window = tkinter.Tk()
        tkinter_frame = self.build_frame(frame_window)

        frame_window.title(self.name)
        frame_window.geometry("400x600")

        tkinter_frame.pack()

        frame_window.mainloop()
    #




    #update ability scores
    def update_ability_scores(self, fnew_ability_scores):
        i = 0
        for each_ability in self.table.abilities.values():
            self.ability_scores[each_ability.id] += fnew_ability_scores[i]
            i += 1

        #refresh speed
        self.speed = self.ability_scores["constitution"] * 2
        
        #update skills
        self.refresh_skill_bases()
        #update hitpoints
        self.refresh_hit_points()
    #end update ability scores



    #update skill ranks
    def update_skill_ranks(self, f_new_ranks):
        i = 0
        for each_skill in self.table.skills.values():
            self.skill_ranks[each_skill.id] += f_new_ranks[i]
            i += 1
        #update skills
        self.refresh_skills()
    #end update skill ranks

    #refresh skill bases, used if ability scores are changed
    def refresh_skill_bases(self):
        for each_skill in self.table.skills.values():
            self.skill_bases[each_skill.id] = (self.ability_scores[each_skill.main_ability.id] + 
                                             self.ability_scores[each_skill.secondary_ability.id])
        #update skill totals
        self.refresh_skills() 
    #end refresh skill bases

    #refresh skill totals, used if ability scores, skill bases, or skill ranks are changed 
    def refresh_skills(self):
        for each_skill in self.table.skills.values():
            self.skills[each_skill.id] = self.skill_bases[each_skill.id] + self.skill_ranks[each_skill.id]
    #end skill refresh



    #refresh hitpoints, used if ability scores change
    def refresh_hit_points(self):
        self.hitpoint_total = (self.ability_scores["size"] + self. ability_scores["constitution"])
        for each_hitbox in self.species.hitboxes:
            self.max_hitpoints[each_hitbox] = int(self.hitpoint_total * (self.species.hitboxes[each_hitbox]/100))
    #end refresh hitpoints



    #add item to inventory
    def collect_item(self, f_item):
        self.inventory[f_item.object_id] = f_item
    #end add item to inventory


    
    #takes damage, subtracts damage from current HP of one hitbox
    def take_damage(self, f_damage, f_hitbox):
        self.current_hitpoints[f_hitbox] -= f_damage
    #end take damage

    #removes damage, adds to current HP
    def heal_damage(self, f_heal, f_hitbox):
        if (int(self.current_hitpoints[f_hitbox] + f_heal) >= 
            int(self.max_hitpoints[f_hitbox]) ):
            self.current_hitpoints[f_hitbox] = self.max_hitpoints[f_hitbox]
        else:
            self.current_hitpoints[f_hitbox] += f_heal
    #end heal

#end player character class

#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 09
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#this file contains the class definitions and methods for abilities 
#   abilites are used by player characters and NPCs to 
#   determine their primary capabilities.
#   Abilities also provide bonuses to skills


#open configuration file
ability_config = open("./player_character/abilities/abilities.gameconfig")


class Ability:
    def __init__(self, f_id, f_name, f_category):
        self.id = f_id
        self.name = f_name
        self.category = f_category
    #end initializer

    #print a skill to the console
    def print_ability(self):
        print("Ability:\t" + str(self.id) + "\n" +
              "Name:\t\t" + str(self.name) + "\n" +
              "Type:\t\t" + str(self.category) + "\n")
    #end print skill

#end skill definition


#load skills from game configuration file
core_abilities = {}
for each_line in ability_config:
    ability_data = str(each_line.replace("\n", "")).split(", ")
    this_ability = Ability(ability_data[0], ability_data[1], ability_data[2])
    core_abilities[this_ability.id] = this_ability
#end load



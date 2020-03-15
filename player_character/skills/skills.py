#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 09
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#this file contains the class definitions and methods for skills 
#   skills are used by player characters and NPCs to 
#   determine the success of tasks performed in the game

import sys
sys.path.append('./player_character/abilities')
import abilities

#open configuration file
skills_config = open("./player_character/skills/skills.gameconfig")

class Skill:
    def __init__(self, f_id, f_name, f_main_ability, f_secondary_ability, f_category, f_specialty = ""):
        self.id = f_id
        self.name = f_name
        self.main_ability = abilities.default_abilities[f_main_ability]
        self.secondary_ability = abilities.default_abilities[f_secondary_ability]
        self.category = f_category
        self.specialty = f_specialty
    #end initializer

    #print a skill to the console
    def print_skill(self):
        print("Skill:\t\t" + str(self.id) + "\n" +
              "Name:\t\t" + str(self.name) + "\n" +
              "Main Abil:\t" + str(self.main_ability.name) + "\n" +
              "Sec Abil:\t" + str(self.secondary_ability.name) + "\n" +
              "Type:\t\t" + str(self.category))
        if (len(self.specialty) > 0):
            print("Specialty:\t" + str(self.specialty))
        print()
    #end print skill

#end skill definition


#load skills from game configuration file
default_skills = {}
for each_line in skills_config:
    skill_data = str(each_line.replace("\n", "")).split(", ")
    skill_traits = []
    for each_item in skill_data:
        skill_traits.append(each_item)
    this_skill = Skill(*skill_traits)
    default_skills[this_skill.id] = this_skill
#end load

"""
    this_skill = Skill(skill_data[0], 
                      skill_data[1], 
                      abilities.core_abilities[skill_data[2]], 
                      abilities.core_abilities[skill_data[3]], 
                      skill_data[4])

"""
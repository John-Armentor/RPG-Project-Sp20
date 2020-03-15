#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 06
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

import player_character
import tkinter
import sys
sys.path.append('./player_character/abilities')
import abilities
sys.path.append('./player_character/skills')
import skills

#ability score parameters
min_ability_score = 5                     #minimum score, starting score at initialization
starting_ability_points_per_score = 10      #this number defines the average points per score at character creation
starting_ability_points = starting_ability_points_per_score * len(abilities.default_abilities)  #total of above
max_ability_score = 20                    #maximum ability score bonus at character creation


#skill rank parameters
min_skill_ranks = 0                #minimum additional points added to each skill besides linked abilities
starting_skill_points = 150        #total character creation points added to skill ranks
max_skill_ranks = 40              #maximux skill bonus allowed at character creation



###################################
#### character creation screen ####
###################################
def character_creation(f_character):
        
    print("Character Creation:")
    print()
    
    #tkinter window for GUI character creation
    character_creation_window = tkinter.Tk() #character creation window
    character_creation_window.title("Character Creation")






    ############ Abilities ############

    #remaining points to spend on abilities
    ability_points_left = starting_ability_points 
    #highest bonus to be added to ability scores
    ability_max_bonus = min(max_ability_score - min_ability_score, 
                          ability_points_left)

    #dictionary used to be converted to list
    #   list will be used as parameters for the character object's
    #   update abilites function
    ability_bonuses = {}
    for each_ability in f_character.table.abilities.values():
        ability_bonuses[each_ability.id] = 0


    #give instructions for adding points to ability scores
    ability_banner = str("Abilities:\nYou have " + str(ability_points_left) + 
                        " points to distribute amongst your ability scores.\n" + 
                        "Each score starts at " + str(min_ability_score) + ".\n" +
                        "The maximum for each score is " + str(max_ability_score) + ".")
    label = tkinter.Label(text = ability_banner).pack()


    #used when the ability score spinbox arrows are clicked, 
    #   updates the bonuses with new value from the spinbox
    def ability_spinbox_update():
        #update ability bonuses based off values in the spinboxes
        for each_ability in f_character.table.abilities.values():
            ability_bonuses[each_ability.id] = int(ability_bonus_spinboxes[each_ability.id].get()) 

        #check how many points are left
        ability_bonus_sum = 0
        for each_ability in f_character.table.abilities.values():
            ability_bonus_sum += ability_bonuses[each_ability.id]
        ability_points_left = starting_ability_points - ability_bonus_sum
        ability_max_bonus = max_ability_score - min_ability_score 

        #don't let player spend more points than they have, resets spinbox max values
        if(ability_points_left == 0):
            for each_ability in f_character.table.abilities.values():
                ability_bonus_spinboxes[each_ability.id].config(to = int(ability_bonus_spinboxes[each_ability.id].get()))

        #reset maximums if player deallocates points or has points left
        else:
            for each_ability in f_character.table.abilities.values():
                ability_bonus_spinboxes[each_ability.id].config(
                    to = min(ability_max_bonus, 
                             int(ability_bonus_spinboxes[each_ability.id].get()) + 
                             ability_points_left))

        #debugging
        #print(abilityBonuses, end="\t")
        #print(abilityPointsLeft, abilityMaxBonus)
    #end ability spinbox update
    
    #add a spinbox user uses to allocate points to each ability score
    ability_bonus_spinboxes = {}
    for each_ability in f_character.table.abilities.values():
        label = tkinter.Label(text = each_ability.name + ":").pack() 
        ability_bonus_spinboxes[each_ability.id] = tkinter.Spinbox(
            character_creation_window, from_ = 0, to = ability_max_bonus, 
            command = ability_spinbox_update)
        ability_bonus_spinboxes[each_ability.id].pack()
    #
    label = tkinter.Label(text="").pack() #blank line

    ###################################






    ############ Skills ############

    #remaining points to spend on skills
    skill_points_left = starting_skill_points
    #highest bonus that can be added to skill ranks
    skill_max_bonus = min(max_skill_ranks - min_skill_ranks, skill_points_left)

    #dictionary used to be converted to list
    #   list will be used as parameters for the character object's
    #   update abilites function
    skill_bonuses = {}
    for each_skill in f_character.table.skills.values():
        skill_bonuses[each_skill.id] = 0


    #give instructions for adding points to skill ranks
    skill_banner = str("Skills:\nYou have " + str(skill_points_left) + " "+ 
                      "points to distribute amongst your skill ranks.\n" + 
                      "Each rank starts at " + str(min_skill_ranks) + ".\n" +
                      "The maximum for each rank is " + str(max_skill_ranks) + ".\n" +
                      "In addition to ranks, each skill gains a bonus from " +
                      "each of its two link Abilities.")
    label = tkinter.Label(text = skill_banner).pack()


    #update skill bonuses when skill spinbox arrows are clicked
    def skill_spinbox_update():
        #update skill bonuses based off values in the spinboxes
        for each_skill in f_character.table.skills.values():
            #if (int(skillBonusSpinboxes[eachSkill[0]].get()) > int(maxSkillRanks)):   #input validation
            #    skillBonusSpinboxes[eachSkill[0]].set(int(maxSkillRanks))
            skill_bonuses[each_skill.id] = int(skill_bonus_spinboxes[each_skill.id].get())

        #check how many points are left for skills
        skill_bonus_sum = 0
        for each_skill in f_character.table.skills.values():
            skill_bonus_sum += skill_bonuses[each_skill.id]
        skill_points_left = starting_skill_points - skill_bonus_sum

        #don't let player spend more points than they have, reset spinbox max values
        """
        if(skillPointsLeft == 0):
            for eachSkill in playerCharacter.coreSkills:
                skillBonusSpinboxes[eachSkill[0]].config(
                    to = int(skillBonusSpinboxes[eachSkill[0]].get()))
        else:
            for eachSkill in playerCharacter.coreSkills:
                skillBonusSpinboxes[eachSkill[0]].config(
                    to = min(skillMaxBonus, 
                             int(skillBonusSpinboxes[eachSkill[0]].get()) + skillPointsLeft))
        """
        for each_skill in f_character.table.skills.values():
            skill_bonus_spinboxes[each_skill.id].config(
                to = min(skill_max_bonus, 
                         int(skill_bonus_spinboxes[each_skill.id].get()) + skill_points_left))


    #end skill spinbox update

    #add a spinbox user uses to allocate points to each skill rank
    skill_bonus_spinboxes = {}
    for each_skill in f_character.table.skills.values():
        label = tkinter.Label(text = str(each_skill.name) + " (" +
                              str(each_skill.main_ability.name) + ", " +
                              str(each_skill.secondary_ability.name) + "):").pack()
        skill_bonus_spinboxes[each_skill.id] = tkinter.Spinbox(character_creation_window, from_ = 0, 
                                                            to = max_skill_ranks,
                                                            command = skill_spinbox_update)
        skill_bonus_spinboxes[each_skill.id].pack()
    #
    label = tkinter.Label(text="").pack() #blank line
    
    ###################################




    character_creation_window.mainloop()
    #end character creation window
        
    #debugging
    #print(abilityBonuses)





    #update scores
    new_ability_scores = []
    for each_ability in f_character.table.abilities.values():
        new_ability_scores.append(ability_bonuses[each_ability.id])
    f_character.update_ability_scores(new_ability_scores)

    new_skill_ranks = []
    for each_skill in f_character.table.skills.values():
        new_skill_ranks.append(skill_bonuses[each_skill.id])
    f_character.update_skill_ranks(new_skill_ranks)

#end character creation function

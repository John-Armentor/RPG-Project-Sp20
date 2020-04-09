#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2020 04 04
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

"""
    This file contain function definitions for commands
        used to facilitate combat rounds and turns
"""

import dice

def attack_action(f_attacker, f_defender, 
                  f_attacker_skill = "unarmed", f_defender_skill = "unarmed", 
                  f_attacker_difficulty = "standard", f_defender_difficulty = "standard",
                  f_attacker_weapon = "unarmed", f_defender_weapon = "unarmed"):


    #initialize parameter of unarmed to character's game item
    if (f_attacker_weapon == "unarmed"):
        f_attacker_weapon = f_attacker.unarmed
    if (f_defender_weapon == "unarmed"):
        f_defender_weapon = f_defender.unarmed #here would be a defenders shield if they had one.


    #attempt opposed combat skill check between attacker and defender
    try:
        skill_results = dice.opposed_check(f_attacker, f_defender, 
                                           f_attacker.skills[f_attacker_skill], f_attacker_difficulty,
                                           f_defender.skills[f_defender_skill], f_defender_difficulty)
    
    except Exception as error:
        print("An error occurred in attack_action when making the skill check:")
        print(error)
        print("Parameters:")
        print(locals())

    else:
        if (skill_results[0] == None): #if no-ne succeeds the attack or parry roll
            print("attack_action: No one succeeded their combat roll.") #debugging

        elif (skill_results[0] == f_attacker):
            print("attack_action: The attack roll was successful.") #debugging

        else:
            print("attack_action: The defender parried.") 

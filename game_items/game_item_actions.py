#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 01
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the all valid actions for game items
#   they are then stored in a dictionary to be added to individual
#   items actions list

import sys
sys.path.append('./game_engine')
import dice


def weapon_attack(f_object, f_source, f_target, f_damage_multiplier = 1, f_target_hitbox = "random"):
    """
    attack take in a weapon or other source of damage, 
        the PC object performing the attack,
        and the PC object being attacked.
    """
    print("ATTACK!") #debugging

    """ set damage type and dice """
    try:
        damage_string = f_object.traits["damage"].split("d")
        num_dice = int(damage_string[0])
        damage_die = int(damage_string[1])

    except Exception as error:
        print("game_item_actions.py > weapon_attack: Error found in attack function:")
        print(error)
        try:
            print("game_item: " + str(f_object.name) +
                  "\nobject_id: " + str(f_object.object_id) +
                  "\nheap_object: " + str(f_object) )
        except Exception as print_error:
            print("Error found printing object info:")
            print(print_error)
    
    else:
        """roll damage"""
        damage = 0
        for each_die in range(num_dice):
            damage += dice.roll_d(damage_die)
        damage *= f_damage_multiplier

        """deal damage"""
        if (f_target_hitbox == "random"):
            target_hitbox = f_target.species.get_random_hitbox()

        else: #if specific location is targeted, search for parameterized hitbox
                target_hitbox = f_target_hitbox
            #
        #

        try:
            f_target.take_damage(damage, target_hitbox) 

        except Exception as error: #if hitbox not found, most likely
            print("Error found when dealing damage searching for target hitbox:")
            print(error)
            print("Using random hitbox instead...")
            target_hitbox = f_target.species.get_random_hitbox()
            f_target.take_damage(damage, target_hitbox) 


        
    #

# end weapon attack


def parry(f_subject = None):
    print("PARRY!")


def explode(f_subject = None):
    print("EXPLODE!")


def drink_healing_potion(f_subject = None):
    if (f_subject != None):
        print(f_subject.name)
        for each_hitbox in f_subject.max_hitpoints:
            f_subject.heal_damage(dice.roll_d(3), each_hitbox)
    print("CHUG!")
#end healing potion


valid_actions = {
                "weapon_attack": weapon_attack, 
                "parry": parry,
                "explode": explode,
                "drink_healing_potion": drink_healing_potion
                } 
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


def attack(f_object, f_source, f_target):
    """
    attack take in a weapon or other source of damage, 
        the PC object performing the attack,
        and the PC object being attacked.
    """
    print("ATTACK!") #debugging





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
                "attack": attack, 
                "parry": parry,
                "explode": explode,
                "drink_healing_potion": drink_healing_potion
                } 
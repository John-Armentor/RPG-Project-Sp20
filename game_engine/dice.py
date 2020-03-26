#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 02
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#this file contains functions to roll dice (produce random numbers)
#   and check for successful rolls against probability likelihoods

import random
import math
import sys


difficulty_grades = {
    "automatic":    sys.maxsize,
    "very_easy":    2.0,
    "easy":         1.5,
    "standard":     1.0,
    "hard":         0.67,
    "formidable":   0.5,
    "herculean":    0.1,
    "hopeless":     -1.0
    }
    
critical_target = 4     #rolling lower than this always succeeds
fumble_target = 96      #rolling higher than this always fails



#roll dice against a given probablity and return success/fail result (boolean)
def roll_check(f_probability, f_difficulty = "standard"):
    target = int(math.floor(float(f_probability) * difficulty_grades[f_difficulty]))
    #print("Target:\t" + str(target))        #debugging

    roll = random.randrange(100) #produces a pseudorandom integer between 0 and 99 inclusively
    #print("Roll:\t" + str(roll))            #debugging

    if (roll > fumble_target):
        #print("Fumble!")        #debugging
        return False
    elif (roll < critical_target):
        #print("Crit!")          #debugging
        return True
    elif (roll < target):
        #print("Success!")       #debugging
        return True
    else:
        #print("Fail!")          #debugging
        return False

#end roll check



#make a skill check given the character, skill name, and optional difficulty
def skill_check(f_character, f_skill, f_difficulty = "standard"):
    prob = f_character.skills[f_skill]
    return roll_check(prob, f_difficulty)
#end skill check



#roll a plain die, not related to a check,
#   useful for damage dice
def roll_d(f_die_size):
    return int((random.randrange(f_die_size-1))+1) #rolls between 1 and die size, inclusively
#end roll d_ 



"""TODO: WIP
#make opposed check
#   both players must roll a success,
#   if only one does then that player wins,
#   else the player who rolls the closest to their 
#   skill but less than their skill wins
def opposed_check(f_p1, f_p2, f_skill1, f_skill2 = f_skill1):
    victor = None
    
    p1_roll = random.randrange(100)
    p2_roll = random.randrange(100)

    #if (p1_roll
    
    return victor
"""



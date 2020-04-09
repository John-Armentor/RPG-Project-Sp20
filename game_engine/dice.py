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
def roll_d(f_die_size = 100):
    return int((random.randrange(f_die_size-1))+1) #rolls between 1 and die size, inclusively
#end roll d_ 



#make opposed check
#   both players must roll a success,
#   if only one does then that player wins,
#   else the player who rolls the closest to their 
#   skill but less than their skill wins
def opposed_check(f_p1, f_p2, 
                  f_skill1 = 50, f_difficulty1 = "standard",
                  f_skill2 = None, f_difficulty2 = None):
    #adjust parameters
    if f_skill2 == None:
        f_skill2 = f_skill1
    if f_difficulty2 == None:
        f_difficulty2 = f_difficulty1

    victor = None
    defeated = None
    
    #roll dice
    p1_roll = random.randrange(100) #produces a pseudorandom integer between 0 and 99 inclusively
    p2_roll = random.randrange(100) #produces a pseudorandom integer between 0 and 99 inclusively

    #get targets modified by any difficulty modifiers
    p1_target = int(math.floor(float(f_skill1) * difficulty_grades[f_difficulty1])) 
    p2_target = int(math.floor(float(f_skill2) * difficulty_grades[f_difficulty2])) 


    #debugging
    display_rolls = True
    if display_rolls:
        print("In dice.py > opposed_check:")
        print("P1 Roll: " + str(p1_roll))
        print("P1 Skill: " + str(p1_target))
        print("P2 Roll: " + str(p2_roll))
        print("P2 Skill: " + str(p2_target))
    

    #if player 1 succeeds and player 2 fails, player 1 wins
    if ( (p1_roll < p1_target) and (p2_roll > p2_target) ):
        victor = f_p1
        defeated = f_p2

    #if player 2 succeeds and player 1 fails, player 2 wins
    elif ( (p2_roll < p2_target) and (p1_roll > p1_target) ):
        victor = f_p2
        defeated = f_p1

    #if both players succeed, the roller closest to their skill difficulty wins
    elif ( (p1_roll < p1_target) and (p2_roll < p2_target) ):
        p1_difference = p1_target - p1_roll
        p2_difference = p2_target - p2_roll

        #if player 1 is closest
        if (p1_difference < p2_difference):
            victor = f_p1
            defeated = f_p2

        #if player 2 is closest
        elif (p2_difference < p1_difference):
            victor = f_p2
            defeated = f_p1

        #if the differences are tied, reroll
        else:
           victor = opposed_check(f_p1, f_p2, f_skill1, f_skill2, f_difficulty1, f_difficulty2)

    #if neither player succeeds
    else:
        victor = None
        defeated = None

    #

    #determine levels of advantage
    advantage = 0
    if victor == f_p1:
        if (p1_roll < p1_target):
            advantage += 1
        if (p1_roll < critical_target):
            advantage += 1
        if (p2_roll > fumble_target):
            advantage += 1
    elif victor == f_p2:
        if (p2_roll < p2_target):
            advantage += 1
        if (p2_roll < critical_target):
            advantage += 1
        if (p1_roll > fumble_target):
            advantage += 1
    #

    return [victor, advantage]

#end opposed check

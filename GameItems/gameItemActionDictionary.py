#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 01
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the all valid actions for game items
#   they are then stored in a dictionary to be added to individual
#   items actions list

def attack():
    print("ATTACK!")

def parry():
    print("PARRY!")

def explode():
    print("EXPLODE!")

valid_actions = {"attack": attack, 
                "parry": parry,
                "explode": explode} 
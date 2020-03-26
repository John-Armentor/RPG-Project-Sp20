#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 03 01
#Course:        CSC424 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the method definitions to save an object 
#   from the game state to the local device and
#   load an object from the local device to the game state.
#   
#   It uses picling via the pickle library to implement this.

import pickle

#save object
def save_object(f_token, f_filename = None):
    folder = "./savefiles/"

    if(f_filename == None):
        filename = str(f_token.object_id)
    else:
        filename = str(f_filename)
    
    filename = str(str(folder) + str(filename) + ".gamesave")

    file = open(filename, "wb")

    pickle.dump(f_token, file)
#

#load object
def load_object(f_filename):

    folder = "./savefiles/"
    filename = str(str(folder) + str(f_filename) + ".gamesave")

    file = open(filename, 'rb')
    object = pickle.load(file)

    return object
#
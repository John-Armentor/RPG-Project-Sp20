############################
# sandbox file for testing #
############################

import sys
sys.path.append('./player_character/')
sys.path.append('./player_character/abilities')
sys.path.append('./player_character/skills')
sys.path.append('./game_items')
sys.path.append('./game_engine')
sys.path.append('./story_items')
sys.path.append('./netcode')

import player_character
import character_creation
import abilities
import skills
import game_item
import game_item_actions
import story_item
import user
import tabletop
import main_menu
import pickler
import chat_message
import dice

import tkinter
import uuid
from functools import partial



print("-------------------------Running sandbox.py-------------------------\n\n")

command = ""

campaign_title = "The Chronicles of Testing"

gm1 = user.User(True)
table1 = tabletop.Tabletop(gm1, campaign_title)
user1 = user.User(False, player_character.PlayerCharacter(table1))


#table1.campaign_name = campaign_title
#table1.player_characters[user1.active_character.object_id] = player_character.PlayerCharacter(table1)
#user1.character.append(table1.player_characters[user1.active_character.object_id])
#user1.active_character = user1.character[0]
#table1.put_on_table(user1)







instructions = ("\n\nsandbox commands:\n" +
                "exit:\tclose the program\n" +
                "help:\tprint list of commands\n" +
                #"AAAAAH!:\trun every command\n" +

                "\n----- Player Character Commands -----\n" +
                "create:\tcreate a new character with gui\n" +
                "abils:\toutput the character's abilities\n" +
                "skills:\toutput the character's skills\n" +
                "bags:\tview the character's inventory\n" +
                "wielded:\tview character's worn and wielded items\n" +
                "charframe:\ttest PC frame builder method\n" +
                #"quick:\tinstantly create a basic character\n" +
                #"sheet:\toutput all the character's stats\n" +

                "\n----- Game Item Commands -----\n" +
                "look:\tview a list of all items in the game items folder\n" +
                "find:\tload some example items and add to inventory\n" +
                "craft:\tbuild a new item with gui\n" +

                "\n----- Story Item Commands -----\n" +
                "story:\tmake a story item with a test image\n" +

                "\n----- Game Engine Commands -----\n" +
                "printskills:\tview all skills in the skills.gameconfig file\n" +
                "printabils:\tview all abilities in the abilities.gameconfig file\n" +
                "table:\tplace the character and a new item on the table and confirm\n" +
                "printtable:\tprint the object ids of al objects on the table\n" +
                "savetable:\tsaves the table to a local file\n" +
                "loadtable:\tloads the table from a local file\n" +
                "main:\topen the main game window\n" +

                "\n----- Dice Commands -----\n" +
                "roll:\tmake a quick dice check (non-skill based)\n" +
                "dicetower:\troll a ton of dice for fun\n" +
                "skillcheck:\tmake a skill check\n" +

                "\n----- Combat Commands -----\n" +
                "thwack:\tattack the PC\n" +
                "chug:\tdrink a healing potion\n" +

                "\n----- Chatlog -----\n" +
                "psst:\tput a chat message on the table and output to console\n" +
                "speak:\tspeak an inputted message and place in chat log\n" + 
                "walk:\tputs a walking action message into the chat log\n" +
                "\n")
print(instructions)



while(command != "exit"):
    command = input()

    #input command switch
    if (command == "exit"):
        break

    #output valid commands for sandbox
    elif (command == "help"):         
        print("-------------------------\n")
        print(instructions)
        print("\n-------------------------\n")







    ##### PC Commands #####

    #tests Character Creation GUI
    elif (command == "create"):    
        print("-------------------------\n")
        character_creation.character_creation(table1.player_characters[user1.active_character.object_id])
        print("\n-------------------------\n")
    
    #ensures ability scores have been updated
    elif (command == "abils"):      
        print("-------------------------\n")
        for each_ability in table1.abilities.values():
            print(str(each_ability.name)+":\t" + 
                  str(table1.player_characters[user1.active_character.object_id].ability_scores[each_ability.id]))
        print("\n-------------------------\n")

    #ensures skills have been updated
    elif (command == "skills"):     
        print("-------------------------\n")
        for each_skill in table1.skills.values():
            print(str(each_skill.name)+":\t" + str(table1.player_characters[user1.active_character.object_id].skills[each_skill.id]))
        print("\n-------------------------\n")

    #view characters inventory
    elif (command == "bags"):       
        print("-------------------------\n")
        for each_item in table1.player_characters[user1.active_character.object_id].inventory.values():
            print(each_item.name)
        print("\n-------------------------\n")

    elif (command == "wielded"):
        print("-------------------------\n")
        for each_item in table1.player_characters[user1.active_character.object_id].item_slots:
            print(str(each_item) + ":\t" + str(table1.player_characters[user1.active_character.object_id].item_slots[each_item]))
        print("\n-------------------------\n")

    elif (command == "charframe"):
        print("-------------------------\n")
        table1.player_characters[user1.active_character.object_id].open_frame()
        print("\n-------------------------\n")






    ##### Game Item Commands #####

    #tests function to get a list of game items from folder
    elif (command == "look"):       
        print("-------------------------\n")
        item_list = game_item.load_items_list()
        for each_item in item_list:
            print(each_item.name)
        print("\n-------------------------\n")

    #tests game item load and print
    elif (command == "find"):       
        print("-------------------------\n")
        iron_sword = game_item.GameItem()
        iron_sword.load_item_from_file(open("./game_items/ironsword.gmitm"))
        iron_sword.print_item()
        table1.player_characters[user1.active_character.object_id].collect_item(iron_sword)
        table1.player_characters[user1.active_character.object_id].item_slots["left_hand"] = table1.player_characters[user1.active_character.object_id].inventory[iron_sword.object_id]
        print("\n")
        journal = game_item.GameItem()
        journal.load_item_from_file(open("./game_items/journal.gmitm"))
        journal.print_item()
        table1.player_characters[user1.active_character.object_id].collect_item(journal)
        print("\n-------------------------\n")

    #tests GUI item creation
    elif (command == "craft"):      
        print("-------------------------\n")
        new_item = game_item.GameItem()
        game_item.game_item_creation(new_item)
        new_item.print_item()
        table1.player_characters[user1.active_character.object_id].collect_item(new_item) #add to inventory

        new_item.open_frame()

        print("\n-------------------------\n")






    ##### Story Item Commands #####

    #make a story item
    elif (command == "story"):
        print("-------------------------\n")
        new_story = story_item.StoryItem()
        #new_story.title = input("Enter Story Item Title:")
        #new_story.message = input("Enter Story Message:")
        new_story.title = "Discovering the Druiddagger"
        new_story.message = "You see a large, mysterious blade before you."
        
        new_story.image_filename = "./images/img001.png"
        new_story.open_frame()
        print("\n-------------------------\n")








    ##### Game Engine Commands #####

    #confirm skills loaded from game config file
    elif (command == "printskills"):
        print("-------------------------\n")
        for each_skill in table1.skills.values():
            each_skill.print_skill()
            print("\n----------\n")
        print("\n-------------------------\n")

    #confirm skills loaded from game config file
    elif (command == "printabils"):
        print("-------------------------\n")
        for each_ability in table1.abilities.values():
            each_ability.print_ability()
            print("\n----------\n")
        print("\n-------------------------\n")

    #put the PC on the table
    elif (command == "table"):
        print("-------------------------\n")
        table1.put_on_table(table1.player_characters[user1.active_character.object_id]) 

        some_item = game_item.GameItem()
        some_item.quick_build()
        print("\n")
        table1.put_on_table(some_item)
        
        for each_character in table1.player_characters.values():
            print(each_character.name) 

        for each_item in table1.game_items.values():
            print(each_item.name)

        print("\n-------------------------\n")

    #open main window
    elif (command == "main"):
        print("-------------------------\n")

        window = main_menu.MainMenu(table1, user1)
        window.mainloop()

        print("\n-------------------------\n")


    #print object ids of all objects on the table
    elif (command == "printtable"):
        print("-------------------------\n")

        table1.print_object_ids()

        print("\n-------------------------\n")

    #save table
    elif (command == "savetable"):
        print("-------------------------\n")

        filename = str(table1.campaign_name.replace(" ", "_"))
        pickler.save_object(table1, filename)

        print("Table Saved!")

        print("\n-------------------------\n")

    #load table
    elif (command == "loadtable"):
        print("-------------------------\n")

        filename = str(table1.campaign_name.replace(" ", "_"))
        table2 = pickler.load_object(filename)
        table2.print_object_ids()

        print("\n-------------------------\n")






    ##### Dice Commands #####

    #make a non skill based check
    elif (command == "roll"):
        print("-------------------------\n")
        prob = input("Enter probability of success:")
        diff = input("Enter difficulty grade:")
        dice.roll_check(prob, diff)
        print("\n-------------------------\n")

    #make a bunch of rolls
    elif (command == "dicetower"):
        print("-------------------------\n")
        for i in range(100):
            dice.roll_check(50)
            print()
        print("\n-------------------------\n")

    #make a skill check
    elif (command == "skillcheck"):
        print("-------------------------\n")
        skill = input("Enter skill to check:")
        dice.skill_check(table1.player_characters[user1.active_character.object_id], skill)
        print("\n-------------------------\n")








    ##### Combat Commands #####
    
    #attack the PC
    elif (command == "thwack"):
        print("-------------------------\n")
        
        dmg = dice.roll_d(4)
        table1.player_characters[user1.active_character.object_id].take_damage(dmg, "abdomen") 
        msg_str = str(table1.player_characters[user1.active_character.object_id].first_name + " has taken " + str(dmg) + " damage!")
        msg = chat_message.ChatMessage(table1.gamemaster, "technical", "public", msg_str)
        table1.put_on_table(msg)
        table1.chatlog[msg.object_id].print_chat_message()
    
        print("\n-------------------------\n")

    #drink a healing potion
    elif (command == "chug"):
        print("-------------------------\n")
        
        #make and collect a potion
        potion = game_item.GameItem()
        potion.load_item_from_file(open("./game_items/healingpotion.gmitm"))
        potion.print_item()
        table1.player_characters[user1.active_character.object_id].collect_item(potion)
        print("\n")

        #take the drink action
        table1.player_characters[user1.active_character.object_id].inventory[potion.object_id].actions["drink_healing_potion"](table1.player_characters[user1.active_character.object_id])
        print()
        
        #add action to chatlog
        msg = chat_message.ChatMessage(table1.player_characters[user1.active_character.object_id], "action", "public", 
                                       "drank a healing potion.")
        table1.put_on_table(msg)
        table1.chatlog[msg.object_id].print_chat_message()
        
        print("\n-------------------------\n")





    ##### Chatlog Commands #####
    
    #create a quick chat message and add to chatlog
    elif (command == "psst"):
        print("-------------------------\n")

        msg = chat_message.ChatMessage(table1.player_characters[user1.active_character.object_id], "speech", "public", "Hello World!")
        table1.put_on_table(msg)
        table1.chatlog[msg.object_id].print_chat_message()

        table1.chatlog[msg.object_id].open_frame()

        print("\n-------------------------\n")

    #create a custom chat message and add to chatlog
    elif (command == "speak"):
        print("-------------------------\n")

        msg = chat_message.ChatMessage(table1.player_characters[user1.active_character.object_id], "speech", "public", 
                                       input("Enter your message..."))
        table1.put_on_table(msg)
        table1.chatlog[msg.object_id].print_chat_message()

        table1.chatlog[msg.object_id].open_frame()

        print("\n-------------------------\n")


    #create an action message and add to chatlog
    elif (command == "walk"):
        print("-------------------------\n")

        msg = chat_message.ChatMessage(table1.player_characters[user1.active_character.object_id], "action", "public", 
                                       "walks forward " + str(table1.player_characters[user1.active_character.object_id].speed) + " feet.")
        table1.put_on_table(msg)
        table1.chatlog[msg.object_id].print_chat_message()

        table1.chatlog[msg.object_id].open_frame()


        print("\n-------------------------\n")

    #invalid command
    else:
        print("Command not valid, enter 'help' to view a list of commands.\n")

#end command switch
        







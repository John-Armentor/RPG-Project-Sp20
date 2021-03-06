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
import character_sheet
import character_creation
import abilities
import skills
import game_item
import game_item_actions
import story_item
import user
import tabletop
import combat
import main_menu
import pickler
import chat_message
import dice
import combat

import tkinter
import uuid
from functools import partial



print("-------------------------Running sandbox.py-------------------------\n\n")

command = ""
campaign_title = "The Chronicles of Testing"
reset = False
save_state = True

filename = str(campaign_title.replace(" ", "_"))
users = []

if reset:
    gm1 = user.User(True)
    table1 = tabletop.Tabletop(gm1, campaign_title)
    users.append(user.User(False, player_character.PlayerCharacter(table1, False), table1))
    #users.append(user.User(False, player_character.PlayerCharacter(table1, True), table1))
    table1.put_on_table(users[0])
    #table1.put_on_table(users[1])

else:
    table1 = pickler.load_object(filename)
    for each_user in table1.users.values():
        users.append(each_user)
        #SANDBOX UPDATE: users[0] replaces user1, users[1] replaces user2
    

#table1.campaign_name = campaign_title
#table1.player_characters[users[0].active_character.object_id] = player_character.PlayerCharacter(table1)
#users[0].character.append(table1.player_characters[users[0].active_character.object_id])
#users[0].active_character = users[0].character[0]


#add image to Etrius
#NOTE: action completed and table saved
#table1.player_characters[users[0].active_character.object_id].image_filename = "./images/halbred_knight.jpg"



instructions = ("\n\nsandbox commands:\n" +
                "exit:\tclose the program (saves if saving is enabled)\n" +
                "help:\tprint list of commands\n" +
                #"AAAAAH!:\trun every command\n" +

                "\n----- Player Character Commands -----\n" +
                "sheet:\topen the character sheet\n" +
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
                "reloadskills:\tresets the table's default skills\n" +
                "printabils:\tview all abilities in the abilities.gameconfig file\n" +
                #"table:\tplace the character and a new item on the table and confirm\n" +
                "printtable:\tprint the object ids of al objects on the table\n" +
                "savetable:\tsaves the table to a local file\n" +
                "loadtable:\tloads the table from a local file\n" +
                "main:\topen the main game window\n" +

                #"\n----- Dice Commands -----\n" +
                #"roll:\tmake a quick dice check (non-skill based)\n" +
                #"dicetower:\troll a ton of dice for fun\n" +
                #"skillcheck:\tmake a skill check\n" +
                #"opposed:\troll a skill check between two opposing characters\n" +

                "\n----- Combat Commands -----\n" +
                "thwack:\tattack the PC (uses take_damage, not weapon_attack)\n" +
                "chug:\tdrink a healing potion\n" +
                "npc:\tadd an NPC to the table (updates users[1])\n" +
                #"engage:\tuse combat.py > attack_action to roll combat between user[0] and an npc\n" + 
                #"combat:\topen the combat window\n" +


                "\n----- Chatlog -----\n" +
                "psst:\tput a chat message on the table and output to console\n" +
                "speak:\tspeak an inputted message and place in chat log\n" + 
                "walk:\tputs a walking action message into the chat log\n" +
                "clearlogs:\tclear chatlog and storylog for debugging\n" +
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

    #tests Character Sheet GUI
    elif (command == "sheet"):
        print("-------------------------\n")
        try:
            character_sheet.character_sheet(table1.player_characters[users[0].active_character.object_id])
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #tests Character Creation GUI
    elif (command == "create"):  
        print("-------------------------\n")
        try:
            character_creation.character_creation(main_menu.MainMenu(table1, users[0]), table1.player_characters[users[0].active_character.object_id])
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")
    
    #ensures ability scores have been updated
    elif (command == "abils"):      
        print("-------------------------\n")
        try:
            for each_ability in table1.abilities.values():
                print(str(each_ability.name)+":\t" + 
                      str(table1.player_characters[users[0].active_character.object_id].ability_scores[each_ability.id]))
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #ensures skills have been updated
    elif (command == "skills"):     
        print("-------------------------\n")
        try:
            for each_skill in table1.skills.values():
                print(str(each_skill.name)+":\t" + str(table1.player_characters[users[0].active_character.object_id].skills[each_skill.id]))
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #view characters inventory
    elif (command == "bags"):       
        print("-------------------------\n")
        try:
            for each_item in table1.player_characters[users[0].active_character.object_id].inventory.values():
                print(each_item.name)
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    elif (command == "wielded"):
        print("-------------------------\n")
        try:
            for each_item in table1.player_characters[users[0].active_character.object_id].item_slots:
                print(str(each_item) + ":\t" + str(table1.player_characters[users[0].active_character.object_id].item_slots[each_item]))
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    elif (command == "charframe"):
        print("-------------------------\n")
        try:
            table1.player_characters[users[0].active_character.object_id].open_frame()
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")






    ##### Game Item Commands #####

    #tests function to get a list of game items from folder
    elif (command == "look"):       
        print("-------------------------\n")
        try:
            item_list = game_item.load_items_list()
            for each_item in item_list:
                print(each_item.name)
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #tests game item load and print
    elif (command == "find"):       
        print("-------------------------\n")
        try:
            iron_sword = game_item.GameItem()
            iron_sword.load_item_from_file(open("./game_items/ironsword.gmitm"))
            iron_sword.print_item()
            table1.player_characters[users[0].active_character.object_id].collect_item(iron_sword)
            table1.player_characters[users[0].active_character.object_id].item_slots["left_hand"] = table1.player_characters[users[0].active_character.object_id].inventory[iron_sword.object_id]
            print("\n")
            journal = game_item.GameItem()
            journal.load_item_from_file(open("./game_items/journal.gmitm"))
            journal.print_item()
            table1.player_characters[users[0].active_character.object_id].collect_item(journal)
        
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #tests GUI item creation
    elif (command == "craft"):      
        print("-------------------------\n")
        try:
            new_item = game_item.GameItem()
            game_item.game_item_creation(new_item)
            new_item.print_item()
            table1.player_characters[users[0].active_character.object_id].collect_item(new_item) #add to inventory

            new_item.open_frame()

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")






    ##### Story Item Commands #####

    #make a story item
    elif (command == "story"):
        print("-------------------------\n")
        try:
            new_story = story_item.StoryItem()
            #new_story.title = input("Enter Story Item Title:")
            #new_story.message = input("Enter Story Message:")
            new_story.title = "Discovering the Druiddagger"
            new_story.message = "You see a large, mysterious blade before you."
        
            new_story.image_filename = "./images/img001.png"
            new_story.open_frame()
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")








    ##### Game Engine Commands #####

    #confirm skills loaded from game config file
    elif (command == "printskills"):
        print("-------------------------\n")
        try:
            for each_skill in table1.skills.values():
                each_skill.print_skill()
                print("\n----------\n")
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #reset the table's default skills according to skills.gameconfig
    elif (command == "resetskills"):
        print("-------------------------\n")
        try:
            table1.skills = skills.load_default_skills()
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #confirm skills loaded from game config file
    elif (command == "printabils"):
        print("-------------------------\n")
        try:
            for each_ability in table1.abilities.values():
                each_ability.print_ability()
                print("\n----------\n")
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #put the PC on the table
    elif (command == "table"):
        print("-------------------------\n")
        try:
            table1.put_on_table(table1.player_characters[users[0].active_character.object_id]) 

            some_item = game_item.GameItem()
            some_item.quick_build()
            print("\n")
            table1.put_on_table(some_item)
        
            for each_character in table1.player_characters.values():
                print(each_character.name) 

            for each_item in table1.game_items.values():
                print(each_item.name)

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #open main window
    elif (command == "main"):
        print("-------------------------\n")
        try:
            window = main_menu.MainMenu(table1, users[0])
            window.mainloop()

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")


    #print object ids of all objects on the table
    elif (command == "printtable"):
        print("-------------------------\n")
        try:
            table1.print_object_ids()

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #save table
    elif (command == "savetable"):
        print("-------------------------\n")
        try:
            filename = str(table1.campaign_name.replace(" ", "_"))
            pickler.save_object(table1, filename)

            print("Table Saved!")

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #load table
    elif (command == "loadtable"):
        print("-------------------------\n")
        try:
            filename = str(table1.campaign_name.replace(" ", "_"))
            table2 = pickler.load_object(filename)
            table2.print_object_ids()

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")






    ##### Dice Commands #####

    #make a non skill based check
    elif (command == "roll"):
        print("-------------------------\n")
        try:
            prob = input("Enter probability of success:")
            diff = input("Enter difficulty grade:")
            dice.roll_check(prob, diff)
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #make a bunch of rolls
    elif (command == "dicetower"):
        print("-------------------------\n")
        try:
            for i in range(100):
                dice.roll_check(50)
                print()
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #make a skill check
    elif (command == "skillcheck"):
        print("-------------------------\n")
        try:
            skill = input("Enter skill to check:")
            dice.skill_check(table1.player_characters[users[0].active_character.object_id], skill)
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #make an opposed roll
    elif (command == "opposed"):
        print("-------------------------\n")
        try:
            winner = dice.opposed_check(table1,
                                        users[0].active_character, 
                                        users[1].active_character, 
                                        input("Enter Player 1 Skill: "),
                                        input("Enter Player 1 Difficulty: "),
                                        input("Enter Player 2 Skill: "),
                                        input("Enter Player 2 Difficulty: ") )
            if winner[0] == None:
                print("Both players failed...")
            else:
                print("The winner is " + str(winner[0].name) + " with " + str(winner[1]) + " levels of advantage.")
                if winner[0].object_id == users[0].active_character.object_id:
                    print("(User 1)")
                if winner[0].object_id == users[1].active_character.object_id:
                    print("(User 2)")

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")








    ##### Combat Commands #####
    
    #attack the PC
    elif (command == "thwack"):
        print("-------------------------\n")
        try:
            dmg = dice.roll_d(4)
            table1.player_characters[users[0].active_character.object_id].take_damage(dmg, "abdomen") 
            msg_str = str(table1.player_characters[users[0].active_character.object_id].first_name + " has taken " + str(dmg) + " damage!")
            msg = chat_message.ChatMessage(table1.gamemaster, "technical", "public", msg_str)
            table1.put_on_table(msg)
            table1.chatlog[msg.object_id].print_chat_message()
    
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #drink a healing potion
    elif (command == "chug"):
        print("-------------------------\n")
        try:
            #make and collect a potion
            potion = game_item.GameItem()
            potion.load_item_from_file(open("./game_items/healingpotion.gmitm"))
            potion.print_item()
            table1.player_characters[users[0].active_character.object_id].collect_item(potion)
            print("\n")

            #take the drink action
            table1.player_characters[users[0].active_character.object_id].inventory[potion.object_id].actions["drink_healing_potion"](table1.player_characters[users[0].active_character.object_id])
            print()
        
            #add action to chatlog
            msg = chat_message.ChatMessage(table1.player_characters[users[0].active_character.object_id], "action", "public", 
                                           "drank a healing potion.")
            table1.put_on_table(msg)
            table1.chatlog[msg.object_id].print_chat_message()
        
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #open the combat window
    elif (command == "combat"):    
        print("-------------------------\n")
        combat.combat(table1, table1.player_characters[user1.active_character.object_id])
        print("\n-------------------------\n")


    elif(command == "npc"):
        print("-------------------------\n")
        try:
            npc = player_character.PlayerCharacter(table1, True)
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            npc.update_name(firstname, lastname)
            character_creation.character_creation(main_menu.MainMenu(table1, table1.gamemaster), npc)
            table1.player_characters[users[1].active_character.object_id] = npc
            users[1].active_character = npc

            welcome = str(npc.name + " has entered the game.")
            msg = chat_message.ChatMessage(table1.gamemaster, "technical", "public", welcome)
            table1.put_on_table(msg)
            table1.chatlog[msg.object_id].print_chat_message()

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")


    elif(command == "engage"):
        print("-------------------------\n")
        try:
            combat.attack_action(table1, users[1].active_character, users[0].active_character)

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")



    ##### Chatlog Commands #####
    
    #create a quick chat message and add to chatlog
    elif (command == "psst"):
        print("-------------------------\n")
        try:
            msg = chat_message.ChatMessage(table1.player_characters[users[0].active_character.object_id], "speech", "public", "Hello World!")
            table1.put_on_table(msg)
            table1.chatlog[msg.object_id].print_chat_message()

            table1.chatlog[msg.object_id].open_frame()

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")

    #create a custom chat message and add to chatlog
    elif (command == "speak"):
        print("-------------------------\n")
        try:
            msg = chat_message.ChatMessage(table1.player_characters[users[0].active_character.object_id], "speech", "public", 
                                           input("Enter your message..."))
            table1.put_on_table(msg)
            table1.chatlog[msg.object_id].print_chat_message()

            table1.chatlog[msg.object_id].open_frame()

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")


    #create an action message and add to chatlog
    elif (command == "walk"):
        print("-------------------------\n")
        try:
            msg = chat_message.ChatMessage(table1.player_characters[users[0].active_character.object_id], "action", "public", 
                                           "walks forward " + str(table1.player_characters[users[0].active_character.object_id].speed) + " feet.")
            table1.put_on_table(msg)
            table1.chatlog[msg.object_id].print_chat_message()

            table1.chatlog[msg.object_id].open_frame()

        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")


    #clear the chatlog and storylog, used only for debugging
    elif (command == "clearlogs"):
        print("-------------------------\n")
        try:
            table1.chatlog = {}
            table1.story_items = {}
            print("Table logs cleared.")
        except Exception as error:
            print("sandbox: error found at " + str(command) + " command:")
            print(error)
        print("\n-------------------------\n")




    #invalid command
    else:
        print("Command not valid, enter 'help' to view a list of commands.\n")

#end command switch
        


#save gamestate for future use
if save_state:
    print("-------------------------\n")
    filename = str(table1.campaign_name.replace(" ", "_"))
    pickler.save_object(table1, filename)
    print("Table Saved!")
    print("\n-------------------------\n")

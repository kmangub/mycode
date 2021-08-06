#!/usr/bin/python3
import sys
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      fight
    ''')

def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    
    print('You are in the ' + currentRoom)
    print('--Life--')
    print(health)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    if "monster" in rooms[currentRoom]:
      print("Heads up, you see a " + rooms[currentRoom]['monster'] + " in the room")
    if "boss" in rooms[currentRoom]:
      print("Uh oh, you see a " + rooms[currentRoom]['boss'] + " in the room. It's charging at you at full speed!")
    print("---------------------------")


health = "\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f"

def checkHealth():
  if health == "":
    print("""You ran out of Health!

    ** Game Over **
    """)
    sys.exit()
#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Forest Dungeon Entrance' : { 
                  'north' : 'Hallway',
                  'south' : "Outside Forest Dungeon",
                },
                
            'Outside Forest Dungeon' : { 
                  'north' : 'Forest Dungeon Entrance',
                },

            'Hallway' : {
                  'south' : 'Forest Dungeon Entrance',
                  'north' : 'Main Room',
                  'monster': 'goblin'
                },
            'Main Room' : {
                  'south' : 'Hallway',
                  'north' : 'Boss Room',
                  'west'  : 'Tunnel',
                  'item'  : 'key'
                },
            'Tunnel'    : {
                  'east'  : 'Main Room',
                  'item'  : 'bow & arrows',
                  'monster': 'poisonous bat'
                }, 
            'Boss Room' : {
                  'south' : 'Main Room',
                  'boss': 'One-Eyed Giant Arachnid',
                  'item'  : 'sacred treasure',
                  'locked': True
                },

         }

#start the player in the Hall
currentRoom = 'Forest Dungeon Entrance'

showInstructions()

#loop forever
while True:  
    checkHealth()
    showStatus()
    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>')
    
    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)
  
    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:

            # Monster Encounter
            if "monster" in rooms[currentRoom].keys():
              print("The " + rooms[currentRoom]["monster"] + " attacked you as you run to the next room. You lost some health.")
              health = health[:-9]

            if "boss" in rooms[currentRoom].keys():
              print("The " + rooms[currentRoom]["boss"] + " was lightning fast and attacked you as you ran to the next room. Big Damage.")
              health = health[:-15]

            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]


            # Unlocking Door
            if rooms["Boss Room"]["locked"] == True and ('key' in inventory):
              rooms["Boss Room"]["locked"] = False
              print("Door Unlocked!")

            # Locked Room Logic
            if rooms["Boss Room"]["locked"] == True and currentRoom == "Boss Room" :
              print("It looks like the door is locked, you need a 'key' to unlock it.")
              currentRoom = rooms["Boss Room"]["south"]
            
            # Winning Criteria with Sacred Treasure in Inventory
            if currentRoom == 'Outside Forest Dungeon' and 'sacred treasure' in inventory:
              print("You escaped with the Sacred Treasure, you win!!")
              break

            if currentRoom == 'Outside Forest Dungeon' and 'sacred treasure' not in inventory:
              while True:
                choice = input('''Are you sure you want to exit the dungeon without the treasure?

[Y]es or [No]
> ''').lower()
                if choice == "y":
                  print("You escaped with the Dungeon without the treasure. Come back when you have mustered up courage.")
                  sys.exit()
                if choice == "n":
                  print("Good, the adventure continues")
                  currentRoom = rooms['Outside Forest Dungeon']['north']
                  break
                else:
                  print("Please enter Y or N")
              


        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
  
    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'fight':
      if "monster" in rooms[currentRoom]:
        if rooms[currentRoom]["monster"] == "poisonous bat":
          if 'bow & arrows' in inventory:
            print("Using your Bow & Arrows. You defeated " + rooms[currentRoom]["monster"] + "!")
            del rooms[currentRoom]['monster']
          else:
            print("You couldn't reach the bat. You took 1 damage.")
            health = health[:-3]
        else:
          print("You swung your sword and defeated " + rooms[currentRoom]["monster"] + ". You only took 1 damage" )
          health = health[:-3]
          del rooms[currentRoom]['monster']
      if "boss" in rooms[currentRoom]:
        if 'bow & arrows' in inventory:
          print("Using your Bow & Arrows. You defeated " + rooms[currentRoom]["boss"] + "!! Now, collect what's yours.")
          del rooms[currentRoom]['boss']
        else:
          print("Oh no, you're sword was no good. You are defeated. Maybe there's an item in the dungeon that can help you out.")
          health = health[:-15]
    



'''
Winning Criteria: Get Sacred Treasure and Escape the Dungeon

Losing Criteria: Health reaches 0
  How to lose health: trap damage, monster damage, oxygen levels


'''

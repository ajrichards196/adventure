import textwrap
from world import WorldRoom, WorldItem
from const import SCREEN_WIDTH
from rooms import rooms
from items import items
from characters import Player
import os

def refreshScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    status_message = f"Health: 100, Location: {current_room.location}"
    print(status_message)
    print('=' * len(status_message))
    print()

def printWelcomeScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to adventure.")
    chosen_name = input("choose a name\n>")
    chosen_race = input("choose a race: [elf, dwarf]\n>")
    if chosen_race not in ['elf', 'dwarf']:
        input("please choose from: ['elf', 'dwarf']\n>")
    global player
    player = Player(chosen_name, chosen_race)

def printCommands():
    print("Available commands:")
    print("\t'quit': Quit the game.")
    print("\t'look': Look in a direction or at an item")
    print("\t'go': Move in a direction")
    print("\t'help': List available commands")

def printItems():
    global current_room
    if len(current_room.items) > 0:
        print("You can see the following items:")
        #item: WorldItem
        for item in current_room.items:
            item_name = item
            item = items[item]
            print(f"{item_name}: ", item.short_desc)
    else:
        print(f"There are no items in the {current_room.location}")

def printLocation():
    global current_room
    print('\n'.join(textwrap.wrap(current_room.long_desc,SCREEN_WIDTH)))
    exits = ", ".join([exit for exit in current_room.exits])
    if len(current_room.exits) == 1:
        print(f"There is an exit {exits}")
    else:
        print(f"There are exits {exits}.")
    printItems()  

def moveDirection(direction: str):
    global current_room 
    if direction in current_room.exits:
        next_room = current_room.exits[direction]
        current_room = rooms[next_room]
          
        refreshScreen()
        print(f"You moved {direction} into {current_room.location}")  
    else:
        print(f"You cannot move {direction}")
        #time.sleep(2)
    #return current_room

starting_room = 'town square'
current_room = rooms[starting_room]

os.system('cls' if os.name == 'nt' else 'clear')
printWelcomeScreen()
print("press any key to start")
input('>')
refreshScreen()
game = True
while game:
        
    print()
    print("choose an action")
    player_command = input('>')
    refreshScreen()
    player_command = player_command.lower().split(' ', 1)
    verb = player_command[0]
    noun = ''
    if len(player_command) > 1:
        noun = player_command[1]
    
    if verb == 'help':
        printCommands()
    elif verb == 'quit':
        print("Thanks for playing!")
        game = False
    elif verb == 'look':
        if not noun:
            printLocation()
        if noun == 'items':
            printItems()
        if noun in items:
            item = items[noun]
            print(f"You inspect the {noun}")
            print(item.long_desc)
    elif verb == 'go':
        if not noun:
            noun = input("Choose a direction; north, east, south, west\n>")
        if noun in ['north', 'east','south','west']:
            moveDirection(noun)
            current_room.event.start()
      
    else:
        print(f"Unknown command: {player_command}")

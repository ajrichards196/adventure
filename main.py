import textwrap
from world import WorldRoom, WorldItem
from const import *
from rooms import generate_world
from items import items
from characters import Player
import os

def refreshScreen(player: Player):
    os.system('cls' if os.name == 'nt' else 'clear')
    status_message = f"Player: {player.name} the {player.race}, Health: {player.health}, Location: {player.current_room.location}, Gold: {player.gold}"
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

    return chosen_name, chosen_race

def printCommands():
    print("Available commands:")
    print("\t'quit': Quit the game.")
    print("\t'look': Look at the current room. 'look items' will show items in the room")
    print("\t'look' + direction: Look at the room in the specified direction")
    print("\t'look' + item name: Look at a specific item")
    print("\t'go': Move in a direction")
    print("\t'inventory': Show the items in your inventory")
    print("\t'help': List available commands")

def printItems(player: Player):
    if len(player.current_room.items) > 0:
        print("You can see the following items:")
        for item_name in player.current_room.items:
            item = items[item_name]
            print(f"{item_name}: ", item.short_desc)
    else:
        print(f"There are no items you can pick up in the {player.current_room.location}")

def printLocation(player: Player):
    print('\n'.join(textwrap.wrap(player.current_room.long_desc,SCREEN_WIDTH)))
    exits = ", ".join([exit for exit in player.current_room.exits])
    if len(player.current_room.exits) == 1:
        print(f"There is an exit {exits}")
    else:
        print(f"There are exits {exits}.")
    printItems(player)  

def moveDirection(player: Player, direction: str, rooms):
    if direction in player.current_room.exits:
        next_room = player.current_room.exits[direction]
        player.previous_room = player.current_room
        player.current_room = rooms[next_room]
          
        refreshScreen(player)
        print(f"You moved {direction} into {player.current_room.location}")  
    else:
        print(f"You cannot move {direction}")


def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    character_creation = printWelcomeScreen()
    player = Player(*character_creation, 
                    strength=10, 
                    armour=10, 
                    health=100, 
                    gold=50,
                    weapon=items["fist"])
    rooms = generate_world(player)
    starting_room = rooms['town square']
    player.current_room = starting_room
    player.previous_room = starting_room
    print("press any key to start")
    input('>')
    refreshScreen(player)
    game = True
    while game:
            
        print()
        print("choose an action *type 'help' for available actions")
        player_command = input('>')
        refreshScreen(player)
        player_command = player_command.lower().split(' ', 1)
        verb = player_command[0]
        noun = ''
        if len(player_command) > 1:
            noun = player_command[1]

        if verb == "inventory":
            print("Inventory:")
            print([item.short_desc for item in player.inventory])
        elif verb == 'help':
            printCommands()
        elif verb == 'quit':
            print("Thanks for playing!")
            game = False
        elif verb == 'look':
            if not noun:
                printLocation(player)
            if noun == 'items':
                printItems(player)
            if noun in items:
                item = items[noun]
                print(f"You inspect the {noun}")
                print(item.long_desc)
            if noun in DIRECTIONS:
                direction = noun
                if direction not in player.current_room.exits:
                    print(f"There is nothing to the {direction}")
                else:
                    next_room = player.current_room.exits[direction]
                    print(f"You look {direction}, you see {rooms[next_room].short_desc.lower()}")
        elif verb == 'go':
            if not noun:
                noun = input("Choose a direction; north, east, south, west\n>")
            if noun in DIRECTIONS:
                moveDirection(player, noun, rooms)
                outcome = player.current_room.event.start()
                refreshScreen(player)
                print(outcome)
                if player.health < 1:
                    game = False
        
        else:
            print(f"Unknown command: {player_command}")

if __name__ == "__main__":
    main()
from world import ShopEvent, CombatEvent, WorldEvent
from characters import Player
from items import *
import os

def refreshScreen(player: Player):
    os.system('cls' if os.name == 'nt' else 'clear')
    status_message = f"Health: {player.health}, Location: {player.current_room.location}, Gold: {player.gold}"
    print(status_message)
    print('=' * len(status_message))
    print()

class TownSquareEvent(WorldEvent):
    def __init__(self, description):
        super().__init__(description)

    def start(self):
        print("A bird flies past")

class GeneralStoreEvent(ShopEvent):
    def __init__(self, description, player: Player):
        super().__init__(description)
        self.player = player
        self.items = {'red potion': {"amount": 2, "value": 20}}

    def start(self):
        if len(self.items) == 0:
            self.complete = True
        if self.complete:
            print("I have nothing more to sell, come back another time.")
        if self.first_trigger:
            print("Welcome stranger, can I interest you in any of these goods")
            for item in self.items:
                print(f"{item} x{self.items[item]['amount']}, cost: {self.items[item]['value']}" )
        else:
            print("Ah, changed your mind have we?")
            for item in self.items:
                print(f"{item}, cost: {self.items[item]['value']}" )
        self.first_trigger = False
        shopping = True
        while shopping:
            print("Type 'buy' to purchase an item")
            print("or type 'leave' to leave the shop")
            choice = input(">")
            if choice.lower() == 'leave':
                self.player.current_room = self.player.previous_room
                shopping = False
                return f'You leave the shop and return to the {self.player.previous_room}'
            elif choice.lower() == 'buy':
                print("Which item do you want to buy?")
                item_to_buy = input(">")
                if item_to_buy in self.items and self.player.gold > items[item].value:
                    self.player.gold -= self.items[item]['value']
                    self.player.inventory.append(items[item_to_buy])
                    self.items[item_to_buy]['amount'] -= 1
                    refreshScreen(self.player)
                    print(f"You bought {item_to_buy}")


        


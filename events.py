from world import ShopEvent, CombatEvent, WorldEvent
from characters import Enemy, Player
from items import *
import os, random

def refreshScreen(player: Player, enemy: Enemy = None):
    os.system('cls' if os.name == 'nt' else 'clear')
    status_message = f"Player: {player.name} the {player.race}, Health: {player.health}, Location: {player.current_room.location}, Gold: {player.gold}"
    print(status_message)
    print('=' * len(status_message))
    print()
    if enemy:
        enemy_status = f"Enemy: {enemy.name} the {enemy.race}, Health: {enemy.health}"
        print(enemy_status)
        print('=' * len(enemy_status))
        print()

def fight(player: Player, enemy: Enemy):
    combat = True
    while combat:
        if enemy.health < 1:
            combat = False
            refreshScreen(player, enemy)
            print(f"You knock the {enemy.race} out and he falls to the ground.")
            choice = input("Take his stuff? y/n\n>")
            choice = choice.lower()
            while choice not in ['y','n']:
                refreshScreen(player, enemy)
                print("Type y or n")
                choice = input("Take his stuff? y/n\n>")
                choice = choice.lower()
            if choice == 'y':
                player.gold += enemy.gold
                taken_items = []
                for item in enemy.inventory:
                    player.inventory.append(items[item])
                    enemy.inventory.remove(item)
                    taken_items.append(item)
                refreshScreen(player, enemy)
                player.current_room = player.previous_room  
                return f"You take {taken_items} and {enemy.gold} gold. You return to the {player.previous_room}"
            else:
                refreshScreen(player, enemy)
                player.current_room = player.previous_room                    
                return f'You quickly leave the tavern and return to the {player.previous_room}'
        if player.health < 1:
            combat = False
            refreshScreen(player, enemy)
            return f"You get knocked out by the old {enemy.race} and thrown into the street. Game over."
        
        damage_mod = random.randint(1,10) / 10
        total_damage = enemy.weapon.damage + (enemy.strength * damage_mod)
        total_damage = int(total_damage)
        player.take_damage(total_damage)
        refreshScreen(player, enemy)
        print(f"The {enemy.race} hits you with his fist, doing {total_damage} damage")
        input("Attack? y/n\n>")
        damage_mod = random.randint(1,10) / 10
        total_damage = player.weapon.damage + (player.strength * damage_mod)
        total_damage = int(total_damage)
        enemy.take_damage(total_damage)
        refreshScreen(player, enemy)
        print(f"You hit the {enemy.race} with your fist, doing {total_damage} damage")
        input("run away? y/n\n>")

    


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
        total_items = sum([self.items[item]['amount'] for item in self.items])
        if total_items == 0:
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
                print(f"{item} x{self.items[item]['amount']}, cost: {self.items[item]['value']}" )
        self.first_trigger = False
        shopping = True
        while shopping:
            print("Type 'buy' to purchase an item")
            print("or type 'leave' to leave the shop")

            choice = input(">")
            total_items = sum([self.items[item]['amount'] for item in self.items])
            if total_items == 0:
                refreshScreen(self.player)
                print("I have nothing more to sell, come back another time.")
                input("Press any key to leave the shop\n>")
                shopping = False
                return f'You leave the shop and return to the {self.player.previous_room}'
            if choice.lower() == 'leave':
                self.player.current_room = self.player.previous_room
                shopping = False
                return f'You leave the shop and return to the {self.player.previous_room}'
            elif choice.lower() == 'buy':
                print("Which item do you want to buy?")
                item_to_buy = input(">")
                if item_to_buy not in self.items:
                    refreshScreen(self.player)
                    print(f"Sorry,we don't have any {item_to_buy}")
                    continue
                elif self.player.gold < self.items[item_to_buy]['value']:
                    refreshScreen(self.player)
                    print(f"It seems you can't afford a {item_to_buy}")
                    continue
                elif self.items[item_to_buy]["amount"] < 1:
                    refreshScreen(self.player)
                    print(f"Sorry, we don't have any {item_to_buy} left")
                else:
                    self.player.gold -= self.items[item]['value']
                    self.player.inventory.append(items[item_to_buy])
                    self.items[item_to_buy]['amount'] -= 1
                    refreshScreen(self.player)
                    print(f"You bought {item_to_buy} for {self.items[item]['value']} gold.")


        
class TavernEvent(CombatEvent):
    def __init__(self, description, player: Player):
        super().__init__(description)
        self.player = player
        self.barbarian = Enemy(
            name="Throgar Chucknuts", 
            race="Barbarian",
            strength=8, 
            armour=2, 
            health=25, 
            gold=10, 
            inventory=["dagger"],
            weapon=items["fist"]
            )

    def start(self):
        if self.barbarian.health < 1:
            self.complete = True
        if self.complete:
            print("The barman stares silently at you until you leave.")
            input(">")
            self.player.current_room = self.player.previous_room
            return f'You quickly leave the tavern and return to the {self.player.previous_room}'
        if self.first_trigger:
            print("You walk up to the bar, the barman looks up from cleaning a tankard.")
            print('"What can I get y...", he begins, then you hear a loud voice from behind you')
            print(f'"OI {self.player.race.upper()}, WUT ARE EWE DOIN ERE"')
            choice = input("Choose to leave or respond\n>")
            choice = choice.lower()
            while choice not in ['leave','respond']:
                refreshScreen(self.player)
                print(f"Unknown option {choice}")
                choice = input("Choose to 'leave' or 'respond'\n>")
                choice = choice.lower()
            if choice == 'leave':
                self.player.current_room = self.player.previous_room
                return f'You quickly leave the tavern and return to the {self.player.previous_room}'
            else:
                refreshScreen(self.player)
                print('"What do you want old man?" you respond. The old barbarian swings a punch at you')
                input("press any key to start combat")
        self.first_trigger = False
        outcome = fight(self.player, self.barbarian)

        return outcome
        # while combat:
        #     if self.barbarian.health < 1:
        #         combat = False
        #         refreshScreen(self.player, self.barbarian)
        #         print("You knock the barbarian out and he falls to the ground.")
        #         choice = input("Take his stuff? y/n\n>")
        #         choice = choice.lower()
        #         while choice not in ['y','n']:
        #             refreshScreen(self.player, self.barbarian)
        #             print("Type y or n")
        #             choice = input("Take his stuff? y/n\n>")
        #             choice = choice.lower()
        #         if choice == 'y':
        #             self.player.gold += self.barbarian.gold
        #             taken_items = []
        #             for item in self.barbarian.inventory:
        #                 self.player.inventory.append(items[item])
        #                 self.barbarian.inventory.remove(item)
        #                 taken_items.append(item)
        #             refreshScreen(self.player, self.barbarian)
        #             self.player.current_room = self.player.previous_room  
        #             return f"You take {taken_items} and {self.barbarian.gold} gold. You return to the {self.player.previous_room}"
        #         else:
        #             refreshScreen(self.player, self.barbarian)
        #             self.player.current_room = self.player.previous_room                    
        #             return f'You quickly leave the tavern and return to the {self.player.previous_room}'
        #     if self.player.health < 1:
        #         combat = False
        #         refreshScreen(self.player, self.barbarian)
        #         return f"You get knocked out by the old barbarian and thrown into the street. Game over."
            
        #     damage_mod = random.randint(1,10) / 10
        #     total_damage = self.barbarian.weapon.damage + (self.barbarian.strength * damage_mod)
        #     total_damage = int(total_damage)
        #     self.player.take_damage(total_damage)
        #     refreshScreen(self.player, self.barbarian)
        #     print(f"The barbarian hits you with his fist, doing {total_damage} damage")
        #     input("Attack? y/n\n>")
        #     damage_mod = random.randint(1,10) / 10
        #     total_damage = self.player.weapon.damage + (self.player.strength * damage_mod)
        #     total_damage = int(total_damage)
        #     self.barbarian.take_damage(total_damage)
        #     refreshScreen(self.player, self.barbarian)
        #     print(f"You hit the barbarian with your fist, doing {total_damage} damage")
        #     input("run away? y/n\n>")
            


            
            
        

from world import WorldRoom, WorldEvent, WorldItem

class Character:
    def __init__(self, 
                 name, 
                 race, 
                 strength:int,
                 armour:int,
                 health:int, 
                 gold:int = 0, 
                 inventory:list[WorldItem] = []
                 ):
        self.name = name
        self.race = race
        self.strength = strength
        self.armour = armour
        self.health = health
        self.inventory = inventory
        self.gold = gold

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount: int):
        self.health += amount

class Player(Character):
    def __init__(self, name, race):
        super().__init__(name, 
                         race, 
                         strength=10, 
                         armour=10, 
                         health=100, 
                         gold=50, 
                         xp=0
                         )
        first_event = WorldEvent("start")
        first_room = WorldRoom("starting room", "The ether before the game starts","empty room", {}, first_event)
        self.current_room = first_room
        self.previous_room = first_room

    def add_to_inventory(self, item):
        self.inventory.append(item)
    

    

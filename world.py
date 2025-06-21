class WorldItem:
    def __init__(self, long_desc, short_desc):
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.takeable = True
        self.takeable_desc = ""
        self.edible = False
        self.edible_desc = ""

class Weapon(WorldItem):
    def __init__(self, long_desc, short_desc, damage):
        super().__init__(long_desc, short_desc)
        self.takeable = True
        self.edible = False
        self.damage = damage

class Potion(WorldItem):
    def __init__(self, long_desc, short_desc, colour):
        super().__init__(long_desc, short_desc)
        self.takeable = True
        self.edible = True
        self.colour = colour
        if colour == 'red':
            self.healing = 10

class WorldEvent:
    def __init__(self, description):
        self.description = description
        self.first_trigger = True
        self.complete = False

    def start(self):
        pass

class ShopEvent(WorldEvent):
    def __init__(self, description):
        super().__init__(description)

class CombatEvent(WorldEvent):
    def __init__(self, description):
        super().__init__(description)

class WorldRoom:
    def __init__(self, location: str, long_desc:str, short_desc:str, exits:dict, items:list[WorldItem] = [], event:WorldEvent = None):
        self.location = location
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.exits = exits
        self.items = items
        self.event = event
        self.visited = False

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise Exception(f"{item} not in room")
        
class Player:
    def __init__(self, name, race, gold, health, strength, armour):
        self.name = name
        self.race = race
        self.gold = gold
        self.health = health
        self.strength = strength
        self.armour = armour


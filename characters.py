class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.health = 100
        self.inventory = []

class Player(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, potion):
        self.health += 10
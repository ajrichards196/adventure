from world import ShopEvent, CombatEvent, Player

class GeneralStoreEvent(ShopEvent):
    def __init__(self, description, player: Player, items:list[str]):
        super().__init__(description)
        self.player = player
        self.items = items

    def start(self):
        if self.complete:
            print("I have nothing more to sell, come back another time.")
        if self.first_trigger:
            print("Welcome stranger, can I interest you in any of these goods")
        else:
            print("Ah, changed your mind have we?")
        self.first_trigger = False
        if len(self.items) == 0:
            self.complete = True
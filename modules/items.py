class Item():
    def __init__(self, name, description):
        
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, damage):
    self.damage = damage
    super().__init__(name, description, value)

"""Basic Weapons in the section"""

class Stone(Weapon):
    def __init__(self):
        super().__init__(name = "Cobble",
                        description = "A fist-sized stone, with which to beat in enemy skulls.",
                        damage = 5)

class Knife(Weapon):
    def __init__(self):
        super().__init__(name = "Knife",
                        description = "A flimsy Knife, intended for slicing meat. Small chance to inflic Bleeding",
                        damage = 10)

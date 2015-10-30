"""This file currently contains a base class for enemies and one enemy subclass. More enemies will be added later,
Seperated by what type of area they can spawn in.(e.g. forest, plains, ruins, dungeons, catacombs, cites, ect.)
Enemies that will spawn in multiple or all places will be placed in this main enemies file."""

class Enemy():
    def __init__(self, name, description, hp, statusEff):
        self.name = name
        self.description = description
        self.hp = hp
        self.statusEff = statusEff
    
        def is_alive(self):
        return self.hp > 0

class TestEnemy(Enemy):
    def __init__(self):
        super().__init__(name = "Test Enemy",
                        description = "This enemy only exists to test the worldspace and combat",
                        hp = 20, statusEff = [0,0,0,0,0])

                        
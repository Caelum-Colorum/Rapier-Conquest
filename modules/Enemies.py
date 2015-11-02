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

                        
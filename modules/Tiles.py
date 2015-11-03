import Items, Enemies

#Abstract base tile
class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()
        
class StartRoom(MapTile):
    def intro_text(self):
        return """
        We forgot to write some lore here, so pretend there's some bullshit backstory.
        Here is a description of your surroundings: Trees. Now go adventure or something, I don't know...
        Just don't stay here because thats boring.
        """
    
    def modify_player(self, player):
        #This room has no actions
        pass

class CityTile(MapTile):
    def intro_text(self):
        raise NotImplementedError()
    def modify_player(self, player):
        raise NotImplementedError()

class Market(CityTile):
    def intro_text(self):
        return """
        You walk into the marketplace of the city, it is filed with shops buying and selling items,
        including weapons, armour, potions, and LOTS of useless junk.
        
        To Purchase any of these items, type Buy [weapons/armour/potions].
        """
    def modify_player(self, player):
        #To do: Code for purchasing from a random selection of items that changes every 100 turns
        pass

class CityStreet(CityTile):
    def intro_text(self):
        return """
        You walk down the city road. People are roaming about, but there is nothing to do here.
        """
    def modify_player(self, player):
        pass

class CityHome(CityTile):
    def intro_text(self):
        return """
        You walk down the city road. There is a house for sale here. Type 'Buy house' to buy it.
        """
    def modify_player(self, player):
        #once again, need to impliment a purchase system
        pass

class CityEdge(CityTile):
    def intro_text(self):
        return """
        You've arrived at the edge of the city.
        """
    def modify_player(self, player):
        pass

#class ForestPath(MapTile):
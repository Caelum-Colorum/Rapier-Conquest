import items, enemies

#Abstract base tile
class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def Type(self, tile_type):
        self.tile_type = tile_type
        
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()


#-----------------------------------------------------------------------------------------------------------
#Tiles in this section are parent classes of game tiles, containing concepts to be used in many tiles


class Purchase(MapTile):
    def player_buy(self, items):
        self.items = items
        #This will contain code for purchases when I work out how to do that
    
    def intro_text(self):
        raise NotImplementedError()
    
    def modify_player(self, player):
        raise NotImplementedError()
    
class CityTile(MapTile):
    def Type(self):
        super().Type(tile_type = 'City')
        
    def intro_text(self):
        raise NotImplementedError()
        
    def modify_player(self, player):
        raise NotImplementedError()


#----------------------------------------------------------------------------
#Tiles from here on may appear in game


class StartRoom(MapTile):
    def intro_text(self):
        return """
        
        """
    
    def modify_player(self, player):
        #This room has no actions
        pass

class Market(CityTile, Purchase):
    def intro_text(self):
        return """
        You walk into the marketplace of the city, it is filed with shops buying and selling items,
        including weapons, armour, potions, and LOTS of useless junk.
        
        To Purchase any of these items, type Buy [weapons/armour/potions].
        """
    
    def modify_player(self, player):
        pass
    
    super.player_buy(items = ['Stone', 'Knife'])
                #To do: Code for purchasing from a random selection of items that changes every 100 turns.

class CityStreet(CityTile):

    def intro_text(self):
        return """
        You walk down the city road. People are roaming about, but there is nothing to do here.
        """
    def modify_player(self, player):
        pass

class CityHome(CityTile,):
    def intro_text(self):
        return """
        You walk down the city road. There is a house for sale here. Type 'Buy house' to buy it.
        """
    def modify_player(self, player):
        #Need a home system, where after buying houses, the player repawns at the nearest. 
        #If the player owns no house, they'll respawn at an inn.
        pass

class CityInn(CityTile):
    def intro_text(self):
        return """
        This part of the street seems happier, as you look around, you find the source.
        A large Tavern and inn. You can stay the night for just $40
        """
    modify_player(self, player):
        pass
    
class CityEdge(CityTile):
    def intro_text(self):
        return """
        You've arrived at the edge of the city.
        """
    def modify_player(self, player):
        pass

class ForestPath(MapTile):
    def intro_text(self):
        return """
        
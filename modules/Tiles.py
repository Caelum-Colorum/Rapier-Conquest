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


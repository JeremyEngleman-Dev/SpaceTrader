from player import *
from library import *
from station import *

class Game:
    def __init__(self, player_name, ship_name): 
        self.player = Player(player_name, ship_name)
        self.library = Library()
        self.score = 0
        self.jumps = 0
        self.current_station = Station(self.library.Wares)

    def jump_to_new_station(self):
        print("Test Jump Button")
        self.current_station = Station(self.library.Wares)
from player import *
from library import *
from station import *
from interface import *

class Game:
    def __init__(self, player_name, ship_name): 
        self.player = Player(player_name, ship_name)
        self.library = Library()
        self.score = 0
        self.jumps = 0
        self.current_station = Station(self.library.Wares)

        self.window = Window((1920,1080))
        self.window.station_view.new_station(self.current_station)
        self.window.wait_for_close()


from player import *
from library import *

class Game:
    def __init__(self, player_name, ship_name):
        player = Player(player_name, ship_name)
        library = Library()
        self.score = 0
        self.jumps = 0
